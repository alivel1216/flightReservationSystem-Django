from django.urls import path
from ReservacionesApp import views
urlpatterns = [
    path('',views.home, name="Home"),
    path('reservaciones',views.reservaciones, name="Reservaciones"),
    path('pagos',views.pagos, name="Pagos"),    
    path('consultas',views.consultas, name="Consultas"),
    path('vuelos',views.consultas, name="Vuelos"),
]
