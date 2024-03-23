# urls.py
from django.urls import path
from agent_dashboard.views import property_list

urlpatterns = [
    path('properties/', property_list, name='property-list'),
    # Add other URL patterns as needed
]
