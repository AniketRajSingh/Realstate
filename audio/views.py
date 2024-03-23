from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import UserSettings

def toggle_audio(request):
    if request.method == 'POST':
        user = request.user
        user_settings = get_object_or_404(UserSettings, user=user)
        user_settings.switch_audio = not user_settings.switch_audio
        user_settings.save()
        return JsonResponse({'switch_audio': user_settings.switch_audio})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
