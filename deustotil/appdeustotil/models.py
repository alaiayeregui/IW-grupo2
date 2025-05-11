from django.db import models

class Empleado(models.Model):
    DNI = models.CharField(max_length=9)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    CIF = models.CharField(max_length=12)
    direccion = models.CharField(max_length=30, default="Sin")
    persona_contacto = models.CharField(max_length=30)
    email_contacto = models.EmailField()
    num_contacto = models.CharField(max_length=12)
    pago = models.CharField(max_length=15, choices=[('Efectivo','efectivo'), ('Cheque','cheque'), ('Transferencia','transferencia'), ('Domiciliación','domiciliación')], default="Transferencia")
    def __str__(self):
        return f"{self.nombre} {self.CIF}"

class Responsable(models.Model):
    DNI = models.CharField(max_length=9)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    cargo = models.CharField(max_length=60)
    fecha_incorporacion = models.DateField()
    def __str__(self):
        return f"{self.DNI} {self.nombre} {self.apellidos}"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(null = True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tareas = models.CharField(max_length=100)
    responsables = models.ManyToManyField(Responsable)
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(null = True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ManyToManyField(Empleado)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length= 5, choices=[("Baja","baja"), ("Media","media"), ("Alta","alta")], default = "baja")
    estado = models.CharField(max_length=10, choices=[("Abierta","abierta"),("Asignada","asignada"), ("En proceso","en proceso"), ("Finalizada","finalizada")], default="Abierta")
    notas = models.TextField(null = True, blank=True)
    def __str__(self):
        return self.nombre

