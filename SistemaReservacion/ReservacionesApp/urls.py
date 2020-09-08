from django.urls import path
from ReservacionesApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"),
    path('reservaciones',views.reservaciones, name="Reservaciones"),
    path('pagos',views.pagos, name="Pagos"),    
    path('consultas',views.consultas, name="Consultas"),
    path('configuracion',views.configuracion, name="Configuracion"),
]
