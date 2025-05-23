# Generated by Django 5.2 on 2025-05-13 20:14

import appdeustotil.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdeustotil', '0003_remove_tarea_responsable_tarea_responsable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('documento', models.FileField(upload_to=appdeustotil.models.ruta_personalizada)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='appdeustotil.proyecto')),
            ],
        ),
    ]
