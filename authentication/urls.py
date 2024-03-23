from django.urls import path
from . import views

urlpatterns = [
    path('signup/agent/', views.agent_signup, name='agent_signup'),
    path('signup/user/', views.user_signup, name='user_signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
]
