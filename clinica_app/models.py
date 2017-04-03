from django.db import models
# Create your models here.


class Paciente(models.Model):
    # blank y null hace que no sea un campo obligatorio
    apellidos_paciente = models.CharField(max_length=50, blank=True, null=True)
    nombre_paciente = models.CharField(max_length=50, blank=True, null=True)
    direccion_paciente = models.CharField(max_length=50, blank=True, null=True)
    dni_paciente = models.CharField(max_length=8, blank=True, null=True)
    # class Meta:
    #verbose_name = 'Paciente'
    #verbose_name_plural = 'Pacientes'

    def __unicode__(self):  # Python 2
        return self.direccion_paciente

    def __str__(self):  # Python 3
        return self.direccion_paciente
