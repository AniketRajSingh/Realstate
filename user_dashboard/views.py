from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from agent_dashboard.models import Property
from .models import Wishlist
from .forms import ChangePasswordForm
from django.contrib.auth import update_session_auth_hash

def user_dashboard(request):
    if hasattr(request.user, 'userprofile'):
        return render(request, 'user_dashboard/user_dashboard.html')
    elif hasattr(request.user, 'agentprofile'):
        return redirect('agent_dashboard')  # Redirect agents to agent dashboard
    else:
        return redirect(reverse('login'))  # Redirect to login if no profile is associated

def user_profile(request):
    if hasattr(request.user, 'userprofile'):
        return render(request, 'user_dashboard/user_profile.html')
    elif hasattr(request.user, 'agentprofile'):
        return redirect('agent_profile')  # Redirect agents to agent dashboard
    else:
        return redirect(reverse('login'))  # Redirect to login if no profile is associated

@login_required
def wishlist(request):
    user_profile = request.user.userprofile
    wishlist_items = Wishlist.objects.filter(user_profile=user_profile).values_list('property', flat=True)
    properties = Property.objects.filter(id__in=wishlist_items)
    return render(request, 'user_dashboard/wishlist.html', {'wishlist_items': properties})

@login_required
def settings(request):
    return render(request, 'user_dashboard/settings.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update session to prevent logout
            update_session_auth_hash(request, user)
            return redirect('password_change_done')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def add_to_wishlist(request, property_id):
    if request.method == 'POST':
        property = get_object_or_404(Property, id=property_id)
        user_profile = request.user.userprofile
        wishlist_item, created = Wishlist.objects.get_or_create(user_profile=user_profile, property=property)
        if created:
            return JsonResponse({'message': 'Added to wishlist successfully'})
        else:
            return JsonResponse({'message': 'Property already in wishlist'})
    else:
        return redirect('properties')

@login_required
def remove_from_wishlist(request, property_id):
    if request.method == 'POST':
        property = get_object_or_404(Property, id=property_id)
        user_profile = request.user.userprofile
        wishlist_item = Wishlist.objects.filter(user_profile=user_profile, property=property).first()
        if wishlist_item:
            wishlist_item.delete()
            return JsonResponse({'message': 'Removed from wishlist successfully'})
        else:
            return JsonResponse({'message': 'Property not in wishlist'})
    else:
        return redirect('properties')

@login_required
@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        # Get the form data from request.POST instead of request.body
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        name = f"{first_name} {last_name}" if first_name and last_name else request.user.first_name
        phone_number = request.POST.get('phone_number')
        permanent_address = request.POST.get('permanent_address')

        user_profile = request.user.userprofile
        user_profile.name = name
        user_profile.phone_number = phone_number
        user_profile.permanent_address = permanent_address
        user_profile.save()

        # Update user model's first name and last name
        if first_name:
            request.user.first_name = first_name
            request.user.save()

        if last_name:
            request.user.last_name = last_name
            request.user.save()

        return JsonResponse({'success': True})
    else:
        return HttpResponseBadRequest("Bad Request: Only POST method is allowed for this endpoint.")


@login_required
@csrf_exempt
def update_profile_picture(request):
    if request.method == 'POST':
        # Retrieve the uploaded file from the request
        profile_image = request.FILES.get('profile_image')

        # Check if the profile image exists and is valid
        if profile_image:
            # Assign the profile image to the user's profile
            user_profile = request.user.userprofile
            user_profile.profile_image = profile_image
            user_profile.save()

            # Return a success JSON response
            return JsonResponse({'success': True})
        else:
            # Return a failure JSON response if no valid profile image was provided
            return JsonResponse({'success': False, 'error': 'Invalid or no profile image provided'}, status=400)
    else:
        # Return a failure JSON response for unsupported HTTP methods
        return HttpResponseBadRequest("Bad Request: Only POST method is allowed for this endpoint.")
