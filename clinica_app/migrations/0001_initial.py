# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_paciente', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
