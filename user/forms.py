from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from user.models import User


class LoginUserForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'id': 'login-email',
        'type': 'email',
        'class': 'form-control',
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'id': 'login-password',
        'type': 'password',
        'class': 'form-control',
    }))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Имя", widget=forms.TextInput(attrs={
        'id': 'login-username',
        'type': 'text',
        'class': 'form-control',
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'id': 'login-email',
        'type': 'email',
        'class': 'form-control',
    }))
    password1 = forms.CharField(label="Пароль1", widget=forms.PasswordInput(attrs={
        'id': 'login-password1',
        'type': 'password',
        'class': 'form-control',
    }))
    password2 = forms.CharField(label="Пароль2", widget=forms.PasswordInput(attrs={
        'id': 'login-password2',
        'type': 'password',
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ['email', 'username']