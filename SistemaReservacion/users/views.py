from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from users.forms import createdUserForm
from ReservacionesApp.urls import urlpatterns
# Create your views here.

def registro(request):
    form =  createdUserForm()
    if request.method =='POST':
        form = createdUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Se creo una cuenta para ' + user)
            
            
    context = {'form':form}
    return render(request, 'users/registro.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request, 'Nombre de usuario o contraseña incorrecta')

    context = {}
    return render(request, 'users/login.html', context)