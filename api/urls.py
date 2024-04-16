# urls.py
from django.urls import path
from .views import property_list, property_details

urlpatterns = [
    path('properties/', property_list, name='property-list'),
    path('properties/<int:property_id>/details/', property_details, name='property_details'),
    # Add other URL patterns as needed
]
