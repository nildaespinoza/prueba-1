# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='apellidos_paciente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='direccion_paciente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
