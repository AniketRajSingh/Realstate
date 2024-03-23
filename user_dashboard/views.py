from django.shortcuts import render, redirect
from django.urls import reverse

def user_dashboard(request):
    if hasattr(request.user, 'userprofile'):
        return render(request, 'user_dashboard/user_dashboard.html')
    elif hasattr(request.user, 'agentprofile'):
        return redirect('agent_dashboard')  # Redirect agents to agent dashboard
    else:
        return redirect(reverse('login'))  # Redirect to login if no profile is associated


def wishlist(request):
    return render(request, 'user_dashboard/wishlist.html')
