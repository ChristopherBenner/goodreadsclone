from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

CLASSES = 'w-full py-4 px-6 rounded-xl'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': CLASSES,
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': CLASSES,
    }))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username',
        'class': CLASSES,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': CLASSES,
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': CLASSES,
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': CLASSES,
    }))
