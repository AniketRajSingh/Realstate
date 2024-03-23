from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from .forms import AgentSignUpForm, UserSignUpForm
from agent_dashboard.models import AgentProfile
from user_dashboard.models import UserProfile

def agent_signup(request):
    if request.method == 'POST':
        form = AgentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            agent_profile = AgentProfile.objects.create(user=user, name=form.cleaned_data['name'], phone_number=form.cleaned_data['phone_number'], email=form.cleaned_data['email'], address=form.cleaned_data['address'], govt_id=form.cleaned_data['govt_id'], locality=form.cleaned_data['locality'])
            auth_login(request, user)
            return redirect('agent_dashboard')
    else:
        form = AgentSignUpForm()
    return render(request, 'authentication/agent_signup.html', {'agent_signup_form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user, name=form.cleaned_data['name'], phone_number=form.cleaned_data['phone_number'], email=form.cleaned_data['email'])
            auth_login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserSignUpForm()
    return render(request, 'authentication/user_signup.html', {'user_signup_form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_authenticated:
                    print('Fuck it works')
                    return redirect('agent_dashboard')
                else:
                    print('Fuck it works too')
                    return redirect('user_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            # Display success message
            messages.success(request, 'An email has been sent with instructions to reset your password.')
    else:
        form = PasswordResetForm()
    return render(request, 'authentication/password_reset.html', {'form': form})
