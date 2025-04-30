from django.contrib import admin
from .models import Empleado, Cliente, Responsable, Proyecto, Tarea

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Responsable)
admin.site.register(Proyecto)
admin.site.register(Tarea)