from django.views.generic import View
from django.shortcuts import render

from .forms import AgendamentoForm


class Agendamento(View):
    tamplete_name = 'agendamento/agendamento.html'

    def get(self, request):
        form = AgendamentoForm()
        print(form)
        return render(request, self.tamplete_name, {'form': form})
