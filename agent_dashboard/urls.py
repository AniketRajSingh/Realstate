from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_dashboard, name='agent_dashboard'),
    path('agent_profile', views.agent_profile, name='agent_profile'),
    path('update-profile/', views.update_profile, name='update_agent_profile'),
    path('update-profile-picture/', views.update_profile_picture, name='update_agent_profile_picture'),
    path('agent_reverification/', views.agent_reverification, name='agent_reverification'),
    path('property/', views.enlist_properties, name='enlist_properties'),
    path('settings/', views.settings, name='settings'),
    path('properties/<int:property_id>/edit/', views.edit_property, name='edit_property'),
]