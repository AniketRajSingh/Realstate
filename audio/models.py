from django.db import models
from django.contrib.auth.models import User

class AudioFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    switch_audio = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
