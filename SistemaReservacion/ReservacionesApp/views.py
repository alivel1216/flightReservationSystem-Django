from django.shortcuts import render, redirect
from django.http import HttpResponse
from ReservacionesApp.models import ReservarForm


# Create your views here.
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




def configuracion(request):
    return render(request, 'ReservacionesApp/configuracion.html')