from django.db import models

class Empleado(models.Model):
    DNI = models.CharField(max_length=9)
    nombre = models.CharField()
    apellidos = models.CharField()
    email = models.EmailField()
    telefono = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Cliente(models.Model):
    nombre = models.CharField()
    CIF = models.CharField()
    dirección = models.CharField()
    persona_contacto = models.CharField()
    email_contacto = models.EmailField()
    num_contacto = models.IntegerField()
    pago = models.CharField(choices={'Efectivo':'efectivo', 'Cheque':'cheque', 'Transferencia':'transferencia', 'Domiciliación': 'domiciliación'})
    def __str__(self):
        return f"{self.nombre} {self.CIF}"

class Proyecto(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField(null = True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tareas = models.CharField()
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField(null = True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsble = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    prioridad = models.CharField(choices={"Baja":"baja", "Media":"media", "Alta":"alta"}, default = "baja")
    estado = models.CharField(choices={"Abierta":"abierta","Asignada":"asignada", "En proceso":"en proceso", "Finalizada":"finalizada"})
    notas = models.TextField(null = True, blank=True)
    def __str__(self):
        return self.nombre

