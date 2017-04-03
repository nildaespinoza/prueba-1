from django.contrib import admin
# Register your models here.
from .forms import PacienteModelForm  # OPCIONAL para ModelForm
from .models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    list_per_page = 5
   #list_display = ("apellidos_paciente", "nombre_paciente")
    list_display = ["apellidos_paciente",
                    "nombre_paciente", "direccion_paciente", "dni_paciente"]
    form = PacienteModelForm       # OPCIONAL para ModelForm
    list_display_links = ["apellidos_paciente"]
    list_editable = ["direccion_paciente"]
    list_editable = ["dni_paciente"]
    search_fields = ["apellidos_paciente", "nombre_paciente", "dni_paciente"]

    # class Meta:            HABILITAR EN MODO NORMAL SIN MODELFORM
    #    model = Paciente    HABILITAR EN MODO NORMAL SIN MODELFORM
admin.site.register(Paciente, PacienteAdmin)
