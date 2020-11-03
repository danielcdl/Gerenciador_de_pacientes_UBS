from datetime import datetime
from datetime import date
from datetime import timedelta

from django.views.generic import View
from django.shortcuts import render

from .models import Agendamento
from .models import Feriado
from .models import DiaIndisponivel
from .forms import AgendamentoForm


class Agendar(View):
    tamplete_name = 'agendamento/agendamento.html'

    def get(self, request):
        form = AgendamentoForm()
        return render(request, self.tamplete_name, {'form': form})


def calendario(request):
    if request.method == 'GET':
        mes = request.GET.get('mes')
        ano = request.GET.get('ano')
        mes = int(mes)
        ano = int(ano)
        data_inicio = date(ano, mes, 1)
        if mes == 12:
            data_fim = date(ano + 1, 1, 1)
        else:
            data_fim = date(ano, mes + 1, 1)


        ultimo_dia = date.weekday(data_fim - timedelta(1))

        agendamentos = list(Agendamento.objetos.filter(data__gte=data_inicio, data__lt=data_fim).values_list('data', flat=True))
        feriados = Feriado.objetos.filter(data__gte=data_inicio, data__lt=data_fim).values_list('data', flat=True)
        dias_indisponiveis = DiaIndisponivel.objetos.filter(data__gte=data_inicio, data__lt=data_fim).values_list('data', flat=True)

        data = data_inicio
        incremento = timedelta(1)
        final = (data_fim - incremento).day

        dias = []
        primeiro_dia = date.weekday(data_inicio)
        semana = (primeiro_dia+1) * [{'data': '', 'status': 'desabilitado', 'motivo': 'mes'}]
        contador = primeiro_dia
        for i in range(final):
            agendados = agendamentos.count(data)
            data_formatada = data.strftime('%d/%m/%Y')
            if contador % 7 == 5:
                semana.append({'data': data_formatada, 'status': 'desabilitado', 'motivo': 'sábado'})
                dias.append(semana)
                semana = []
            elif contador % 7 == 6:
                semana.append({'data': data_formatada, 'status': 'desabilitado', 'motivo': 'domingo'})
            elif data in feriados:
                semana.append({'data': data_formatada, 'status': 'desabilitado', 'motivo': 'feriado'})
            elif data in dias_indisponiveis:
                semana.append({'data': data_formatada, 'status': 'desabilitado', 'motivo': 'indisponível'})
            else:
                semana.append({'data': data_formatada, 'status': 'disponivel', 'motivo': agendados})

            if i == final - 1 and contador % 7 != 5:
                dias.append(semana)
            data += incremento
            contador += 1

        return render(request, 'agendamento/calendario.html', {'calendario': dias})
