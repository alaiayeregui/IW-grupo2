# Generated by Django 5.2 on 2025-05-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdeustotil', '0012_alter_proyecto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='codigo',
            field=models.CharField(blank=True, default='', null=True),
        ),
    ]
