from django.urls import path
from PagosApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.pagos, name="Pagos"),
    
]
