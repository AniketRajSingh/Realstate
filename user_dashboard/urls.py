from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('settings/', views.settings, name='settings'),
    path('add-to-wishlist/<int:property_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:property_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('update-profile-picture/', views.update_profile_picture, name='update_profile_picture'),
    path('change-password/', views.change_password, name='change_password'),
]