from django.shortcuts import render

from .forms import PacienteForm
from .models import Paciente
# Create your views here.


def inicio(request):
    form = PacienteForm(request.POST or None)  # campos obligatorios
    # print (dir(form)) parasaber comandos en cmd
    if form.is_valid():
        form_data = form.cleaned_data
        aba = form_data.get("apellidos_paciente")
        abb = form_data.get("nombre_paciente")
        abc = form_data.get("direccion_paciente")
        abd = form_data.get("dni_paciente")
        obj = Paciente.objects.create(apellidos_paciente=aba, nombre_paciente=abb, direccion_paciente=abc, dni_paciente=abd)
    context={
        "var_form": form,
    }
    return render(request, "inicio.html", context)
