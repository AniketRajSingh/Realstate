from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('properties/', views.properties, name='properties'),
    path('property-details/', views.property_details, name='property_details'),
    path('contact/', views.contact, name='contact'),
]