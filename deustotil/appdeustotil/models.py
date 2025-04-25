from django.db import models

class Empleado(models.Model):
    DNI = models.CharField()
    nombre = models.CharField()
    apellidos = models.CharField()
    email = models.EmailField()
    telefono = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField()
    CIF = models.CharField()
    dirección = models.CharField()
    persona_contacto = models.CharField()
    email_contacto = models.EmailField()
    num_contacto = models.IntegerField()
    pago = models.CharField(choices={'efectivo':'efectivo', 'cheque':'cheque', 'transferencia':'transferencia', 'domiciliación': 'domiciliación'})


class Proyecto(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField(null = True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tareas = models.CharField()

class Tarea(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField(null = True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsble = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    prioridad = models.CharField(choices={"alta":"alta", "media":"media", "alta":"alta"})
    estado = models.CharField(choices={"abierta":"abierta","asignada":"asignada", "en proceso":"en proceso", "finalizada":"finalizada"})
    notas = models.TextField(null = True, blank=True)

