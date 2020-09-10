from django.shortcuts import render
#from PagosApp.models import Vuelos 
# Create your views here.

def pagos(request):
    return render(request, 'PagosApp/pagos.html')