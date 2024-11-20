from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from user.models import User
from organization.models import Organization


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


class AddOgrnForm(forms.Form):
    ogrn = forms.CharField(label="OGRN", widget=forms.TextInput(attrs={
        'id': 'id_add_ogrn',
        'type': 'text',
        'class': 'form-control',
    }))

    def clean_ogrn(self):
        ogrn = self.cleaned_data.get('ogrn')
        if len(ogrn) != 13:
            raise ValidationError("OGRN должен быть длиной 13 символов.")
        elif not ogrn.isdigit():
            print('в строке символы')
            raise ValidationError("OGRN должен содержать только цифры.")
        return ogrn
