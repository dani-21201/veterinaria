from django.contrib import admin
from .models import NombreAnimal, Caracteristica, CitasAnimales ,Raza ,NombreDueño ,Historial
# Register your models here.
admin.site.register(NombreAnimal)
admin.site.register(Caracteristica)
admin.site.register(CitasAnimales)
admin.site.register(Raza)
admin.site.register(NombreDueño)
admin.site.register(Historial)
