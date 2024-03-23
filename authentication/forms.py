from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# For AgentSignUpForm
class AgentSignUpForm(UserCreationForm):
    # Add your agent sign-up form fields here
    # For example:
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    govt_id = forms.CharField(max_length=50)
    locality = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'phone_number', 'email', 'address', 'govt_id', 'locality']
        # Adjust as needed

# For UserSignUpForm
class UserSignUpForm(UserCreationForm):
    # Add your user sign-up form fields here
    # For example:
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'phone_number', 'email']
        # Adjust as needed
