from django.shortcuts import render
from audio.models import UserSettings
from agent_dashboard.models import Property

def home(request):
    if request.user.is_authenticated:
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    else:
        user_settings = None
    most_viewed_property = Property.objects.order_by('-views').first()
    return render(request, 'index.html', {'user_settings': user_settings, 'most_viewed_property': most_viewed_property})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')