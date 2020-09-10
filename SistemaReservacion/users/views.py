from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from users.forms import createdUserForm
# Create your views here.

def registro(request):
    form =  UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'users/registro.html', context)

def login(request):
    context = {}
    return render(request, 'users/login.html', context)