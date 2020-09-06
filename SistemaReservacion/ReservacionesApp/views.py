from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'ReservacionesApp/index.html')

def reservaciones(request):
    return render(request, 'ReservacionesApp/reservas.html')

def pagos(request):
    return render(request, 'ReservacionesApp/pagos.html')

def consultas(request):
    return HttpResponse("Consultas")

def vueloss(request):
    return HttpResponse("Vuelos")