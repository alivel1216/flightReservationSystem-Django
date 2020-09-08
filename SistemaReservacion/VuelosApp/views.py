from django.shortcuts import render
from VuelosApp.models import Vuelos 
# Create your views here.

def vuelos(request):
    vuelos=Vuelos.objects.all()
    return render(request, 'VuelosApp/vuelos.html',{"vuelos":vuelos})
