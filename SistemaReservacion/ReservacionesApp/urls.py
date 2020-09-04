from django.urls import path
from ReservacionesApp import views
urlpatterns = [
    path('',views.reservaciones, name="Reservaciones"),
    path('pagos',views.pagos, name="Pagos"),    
    path('consultas',views.consultas, name="Consultas"),
]
