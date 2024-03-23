from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'userprofile_id','name', 'phone_number', 'email')
    search_fields = ('name', 'phone_number', 'email', 'userprofile_id')
    list_filter = ('name', 'phone_number', 'email')
    readonly_fields = ('userprofile_id',)

admin.site.register(UserProfile, UserProfileAdmin)