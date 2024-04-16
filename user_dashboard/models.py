from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from agent_dashboard.models import Property
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='user_profiles/', null=True, blank=True)
    permanent_address = models.TextField()
    userprofile_id = models.CharField(max_length=15, unique=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.userprofile_id = 'USR' + get_random_string(length=4) + self.name[:3].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_profile', 'property')

class RecentlyViewed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'property')
        ordering = ['-viewed_at']

    def __str__(self):
        return f"{self.user.username} viewed {self.property.name}"