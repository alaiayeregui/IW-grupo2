# Generated by Django 5.2 on 2025-04-25 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField()),
                ('CIF', models.CharField()),
                ('dirección', models.CharField()),
                ('persona_contacto', models.CharField()),
                ('email_contacto', models.EmailField(max_length=254)),
                ('num_contacto', models.IntegerField()),
                ('pago', models.CharField(choices=[('Efectivo', 'efectivo'), ('Cheque', 'cheque'), ('Transferencia', 'transferencia'), ('Domiciliación', 'domiciliación')])),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=9)),
                ('nombre', models.CharField()),
                ('apellidos', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('presupuesto', models.FloatField()),
                ('tareas', models.CharField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdeustotil.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('prioridad', models.CharField(choices=[('Baja', 'baja'), ('Media', 'media'), ('Alta', 'alta')], default='baja')),
                ('estado', models.CharField(choices=[('Abierta', 'abierta'), ('Asignada', 'asignada'), ('En proceso', 'en proceso'), ('Finalizada', 'finalizada')])),
                ('notas', models.TextField(blank=True, null=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdeustotil.proyecto')),
                ('responsble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdeustotil.empleado')),
            ],
        ),
    ]
