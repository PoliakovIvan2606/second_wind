from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginUserForm, RegistrationForm, AddOgrnForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = RegistrationForm()

    return render(request, 'user/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        # ogrn = request.POST['ogrn']
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'ok'})  # Перенаправление после успешного логина
            else:
                form.add_error(None, "Неверный email или пароль.")
    else:
        ogrn_form = AddOgrnForm()
        user_form = LoginUserForm()

    return render(request, 'user/login.html', {
        'formUser': user_form,
        'formOgrn': ogrn_form
        })

class LogoutUser(LogoutView):
    success_url = reverse_lazy('user:login')

