from django.contrib import admin
from .models import Property, AgentProfile

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id','property_id', 'name', 'type', 'seller_name', 'price', 'locality', 'contact', 'pincode')
    list_filter = ('type',)
    search_fields = ('name', 'type', 'locality', 'seller_name','contact','property_id')

admin.site.register(Property, PropertyAdmin)

class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'approval_status')
    list_filter = ('approval_status',)
    search_fields = ('name', 'approval_status')
    ordering = ('-id',)

admin.site.register(AgentProfile, AgentProfileAdmin)