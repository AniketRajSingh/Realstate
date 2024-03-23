from django.urls import path
from . import views

urlpatterns = [
    path('', views.toggle_audio, name='toggle_audio'),
]