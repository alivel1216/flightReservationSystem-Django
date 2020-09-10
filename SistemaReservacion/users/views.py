from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def registro(request):
    context = {}
    return render(request, 'users/registro.html', context)

def login(request):
    context = {}
    return render(request, 'users/login.html', context)