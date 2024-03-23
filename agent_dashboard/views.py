from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Property
from .serializers import PropertySerializer
from django.shortcuts import render, redirect
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

