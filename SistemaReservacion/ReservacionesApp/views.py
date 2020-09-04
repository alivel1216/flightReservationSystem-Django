from django.shortcuts import render, HttpResponse

# Create your views here.
#def home(request):
    #return render(request, 'ReservacionesApp/home.html')

def reservaciones(request):
    return render(request, 'ReservacionesApp/home.html')

def pagos(request):
    return HttpResponse("Pagos")

def consultas(request):
    return HttpResponse("Consultas")
