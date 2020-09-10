from django.urls import path
from ReservacionesApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"),
    path('reservaciones',views.reservaciones, name="Reservaciones"),    
    path('consultas',views.consultas, name="Consultas"),
]
