from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'property_image', 'lat', 'lng', 'type', 'description', 'price', 'seller_name', 'locality', 'contact', 'pincode', 'bedrooms', 'bathrooms', 'kitchens', 'floor', 'area']