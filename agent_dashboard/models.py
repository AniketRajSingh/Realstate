from django.db import models
from django.utils.crypto import get_random_string
import random
from django.contrib.auth.models import User

class Property(models.Model):
    TYPE_CHOICES = [
        ('Residential', 'Residential'),
        ('Agricultural', 'Agricultural'),
        ('Commercial', 'Commercial'),
        ('Other', 'Other'),
        # Add more types as needed
    ]

    property_id = models.CharField(max_length=100, unique=True, editable=False)
    name = models.CharField(max_length=100)
    property_image = models.ImageField(upload_to='Properties/', null=True, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    price = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    kitchens = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.property_id:
            # Generate a unique property_id if it doesn't exist
            random_number = random.randint(100, 999)  # Generate a random 3-digit number
            random_string = get_random_string(length=3).upper()  # Generate a random string of length 3
            self.property_id = f'INFK{random_number}{random_string}'  # Concatenate the parts to form the property_id
        super(Property, self).save(*args, **kwargs)


class AgentProfile(models.Model):

    APPROVAL_CHOICES = [
        ('Pending', 'Profile Review Pending'),
        ('Approved', 'Agent Profile Approved'),
        ('Suspended', 'Agent Profile Suspended'),
    ]
    approval_status = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default='Pending')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='agent_profiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    govt_id = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    agent_id = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        # Generate agent ID
        if not self.agent_id:
            govt_id_digits = self.govt_id[-5:]
            agent_id_digits = ''.join(filter(str.isdigit, govt_id_digits))
            locality_chars = self.locality[:3].upper()
            self.agent_id = 'AG' + agent_id_digits + locality_chars
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
