from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

#for logged in users
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full px-6 py-4 rounded-xl'
    }))

#for signup users
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','gender','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full px-6 py-4 rounded-xl'
    }))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={
        'placeholder': 'Select your gender',
        'class': 'w-full px-6 py-4 rounded-xl',
    }))


    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Your email adress",
        'class': 'w-full px-6 py-4 rounded-xl'

    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
        'class': 'w-full px-6 py-4 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm Password",
        'class': 'w-full px-6 py-4 rounded-xl'
    }))
