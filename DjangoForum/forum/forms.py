from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']

        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

