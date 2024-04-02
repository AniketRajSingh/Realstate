from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_dashboard, name='agent_dashboard'),
    path('/agent_profile', views.agent_profile, name='agent_profile'),
]