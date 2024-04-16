from django.http import HttpResponseBadRequest, JsonResponse
from .models import Property
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from user_dashboard.models import RecentlyViewed
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import PropertyForm



def agent_dashboard(request):
    recently_enlisted_properties = Property.objects.filter(enlisted_by=request.user).order_by('-id')[:6]
    property_types = Property.TYPE_CHOICES 
    if hasattr(request.user, 'agentprofile'):
        return render(request, 'agent_dashboard/agent_dashboard.html',{'recently_enlisted_properties': recently_enlisted_properties,'property_types': property_types})
    elif hasattr(request.user, 'userprofile'):
        return redirect('user_dashboard')  # Redirect regular users to user dashboard
    else:
        return redirect(reverse('login'))  # Redirect to login if no profile is associated

def agent_profile(request):
    if hasattr(request.user, 'agentprofile'):
        return render(request, 'agent_dashboard/agent_profile.html')
    elif hasattr(request.user, 'userprofile'):
        return redirect('user_profile')  # Redirect regular users to user dashboard
    else:
        return redirect(reverse('login'))  # Redirect to login if no profile is associated

def agent_reverification(request):
    return render(request, 'agent_dashboard/agent_reverification')
    
@login_required
def enlist_properties(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.enlisted_by = request.user
            property.save()
            return redirect('enlist_properties')
    else:
        form = PropertyForm()

    recently_enlisted_properties = Property.objects.filter(enlisted_by=request.user)
    property_types = Property.TYPE_CHOICES 
    context = {
        'form': form,
        'recently_enlisted_properties': recently_enlisted_properties,
        'property_types': property_types,
    }
    return render(request, 'agent_dashboard/enlist_properties.html', context)

@login_required
def edit_property(request, property_id):
    # Fetch the property object from the database
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        # Populate the form with the POST data and files
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            # Save the form data to update the property
            form.save()
            return JsonResponse({'success': True})
        else:
            # Return any form errors
            return JsonResponse({'success': False, 'errors': form.errors})
    
@login_required
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, enlisted_by=request.user)
    if request.method == 'POST':
        property.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def properties(request):
    properties_list = Property.objects.all()
    paginator = Paginator(properties_list, 6)  # Show 6 properties per page

    page = request.GET.get('page')
    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page
        properties = paginator.page(paginator.num_pages)

    context = {
        'properties': properties
    }
    return render(request, 'property-grid.html', context)

@login_required
def property_details(request, property_id):
    property = get_object_or_404(Property, property_id=property_id)
    context = {
        'property': property
    }
    if request.user.is_authenticated:
        recently_viewed, created = RecentlyViewed.objects.get_or_create(
            user=request.user,
            property=property,
            defaults={'viewed_at': timezone.now()}
        )

        if not created:
            # If the property was previously viewed, update the viewed_at timestamp
            recently_viewed.viewed_at = timezone.now()
            recently_viewed.save()

        # Increment the views count for the property
        if created:
            property.views += 1
            property.save()
        
        return render(request, 'property-single.html', context)

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
        locality = request.POST.get('locality')
        email = request.POST.get('email')

        print(first_name, last_name, phone_number, permanent_address, locality, email)

        agentprofile = request.user.agentprofile
        agentprofile.name = name   
        agentprofile.email = email
        agentprofile.phone_number = phone_number
        agentprofile.locality = locality
        agentprofile.address = permanent_address
        agentprofile.save()

        # Update user model's first name and last name
        if first_name:
            request.user.first_name = first_name
            request.user.save()

        if last_name:
            request.user.last_name = last_name
            request.user.save()

        return redirect(agent_profile)
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
            agent_profile = request.user.agentprofile
            agent_profile.profile_image = profile_image
            agent_profile.save()

            # Return a success JSON response
            return JsonResponse({'success': True})
        else:
            # Return a failure JSON response if no valid profile image was provided
            return JsonResponse({'success': False, 'error': 'Invalid or no profile image provided'}, status=400)
    else:
        # Return a failure JSON response for unsupported HTTP methods
        return HttpResponseBadRequest("Bad Request: Only POST method is allowed for this endpoint.")

@login_required
def settings(request):
    return render(request, 'agent_dashboard/settings.html')