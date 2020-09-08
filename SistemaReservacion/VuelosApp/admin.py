from django.contrib import admin
from .models import Vuelos

# Register your models here.

class vuelosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Vuelos, vuelosAdmin)
