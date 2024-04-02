from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Property
from .serializers import PropertySerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

@api_view(['GET'])
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)

def agent_dashboard(request):
    if hasattr(request.user, 'agentprofile'):
        return render(request, 'agent_dashboard/agent_dashboard.html')
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

def property_details(request, property_id):
    property = get_object_or_404(Property, property_id=property_id)
    context = {
        'property': property
    }
    return render(request, 'property-single.html', context)
