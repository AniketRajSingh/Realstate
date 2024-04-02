from django.urls import path
from . import views
from agent_dashboard.views import properties, property_details

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('properties/', properties, name='properties'),
    path('property-details/<str:property_id>/', property_details, name='property_details'),
    path('contact/', views.contact, name='contact'),
]