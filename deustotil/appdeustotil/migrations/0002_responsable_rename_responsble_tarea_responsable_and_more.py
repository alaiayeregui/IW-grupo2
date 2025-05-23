# Generated by Django 5.1.7 on 2025-04-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdeustotil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=60)),
                ('cargo', models.CharField(max_length=60)),
                ('fecha_incorporacion', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='responsble',
            new_name='responsable',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='dirección',
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default='Sin', max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='CIF',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='num_contacto',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pago',
            field=models.CharField(choices=[('Efectivo', 'efectivo'), ('Cheque', 'cheque'), ('Transferencia', 'transferencia'), ('Domiciliación', 'domiciliación')], default='Transferencia', max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='persona_contacto',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellidos',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='tareas',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('Abierta', 'abierta'), ('Asignada', 'asignada'), ('En proceso', 'en proceso'), ('Finalizada', 'finalizada')], default='Abierta', max_length=10),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.CharField(choices=[('Baja', 'baja'), ('Media', 'media'), ('Alta', 'alta')], default='baja', max_length=5),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='responsables',
            field=models.ManyToManyField(to='appdeustotil.responsable'),
        ),
    ]
