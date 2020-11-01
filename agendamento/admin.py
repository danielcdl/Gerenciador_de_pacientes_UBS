from django.contrib import admin
from .models import Agendamento, Feriado, DiaIndisponivel


admin.site.register(Agendamento)
admin.site.register(Feriado)
admin.site.register(DiaIndisponivel)
