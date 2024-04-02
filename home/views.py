from django.shortcuts import render
from audio.models import UserSettings

def home(request):
    if request.user.is_authenticated:
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    else:
        user_settings = None
    return render(request, 'index.html', {'user_settings': user_settings})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')