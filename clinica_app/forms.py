from django import forms

from .models import Paciente  # OPCIONAL para ModelForm


class PacienteModelForm(forms.ModelForm):  # OPCIONAL para ModelForm

    class meta:  # OPCIONAL para ModelForm
        model = Paciente  # OPCIONAL para ModelForm
        fields = ["apellidos_paciente", "nombre_paciente",
                  "direccion_paciente", "dni_paciente"]  # OPCIONAL para ModelForm


class PacienteForm(forms.Form):
    apellidos_paciente = forms.CharField(max_length=50)
    nombre_paciente = forms.CharField(max_length=50)
    direccion_paciente = forms.CharField(max_length=50)
    dni_paciente = forms.CharField(max_length=8)
