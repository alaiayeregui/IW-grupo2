from django.contrib import admin
from .models import Empleado, Cliente, Proyecto, Tarea

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Tarea)