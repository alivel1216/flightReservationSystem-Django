from django.shortcuts import render, redirect
from django.http import HttpResponse
from ReservacionesApp.models import ReservarForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='Login')
def home(request):
    return render(request, 'ReservacionesApp/index.html')

def reservaciones(request):
    form = ReservarForm()
    if request.method == 'POST':
        form = ReservarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'ReservacionesApp/reservas.html', context)



def consultas(request):
    return render(request, 'ReservacionesApp/consultas.html')

