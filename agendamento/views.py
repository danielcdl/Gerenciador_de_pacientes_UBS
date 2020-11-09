from datetime import date
from datetime import datetime
from datetime import timedelta

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

from pacientes.models import Paciente
from .forms import AgendamentoForm
from .models import Agendamento
from .models import DiaIndisponivel
from .models import Feriado


class Index(TemplateView):
    hoje = datetime.now()
    template_name = 'agendamento/index.html'
    extra_context = {'mes': hoje.month, 'ano': hoje.year}


class Calendario(View):
    context = {}

    def get(self, request, **kargs):
        profissional = kargs['profissional']
        validar_profissional(profissional)
        self.context['profissional'] = profissional

        hoje = datetime.now().date()

        if 'mes' and 'ano' in kargs:
            validar_data(f"01-{kargs['mes']}-{kargs['ano']}")
            mes = int(kargs['mes'])
            ano = int(kargs['ano'])
        else:
            mes = hoje.month
            ano = hoje.year

        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

        self.context['mes'] = meses[mes - 1]
        self.context['ano'] = ano

        data_inicio = date(ano, mes, 1)
        data_fim = date(ano, mes + 1, 1) if mes != 12 else date(ano + 1, 1, 1)

        agendamentos = list(Agendamento.objetos.filter(profissional=profissional, data__gte=data_inicio,
                                                       data__lt=data_fim).values_list('data', 'turno'))
        feriados = list(Feriado.objetos.filter(data__gte=data_inicio, data__lt=data_fim).values_list('data', flat=True))
        dias_indisponiveis = list(
            DiaIndisponivel.objetos.filter(data__gte=data_inicio, data__lt=data_fim).values_list('data', flat=True))

        incremento = timedelta(1)
        final = (data_fim - incremento).day

        self.context['anterior'] = {'mes': (data_inicio - incremento).strftime('%m'),
                                    'ano': (data_inicio - incremento).strftime('%Y')}
        self.context['proximo'] = {'mes': data_fim.strftime('%m'), 'ano': data_fim.strftime('%Y')}

        dias = []
        primeiro_dia = date.weekday(data_inicio)
        if primeiro_dia != 6:
            semana = (primeiro_dia + 1) * [{'data': '', 'status': 'desabilitado', 'motivo': 'mes'}]
        else:
            semana = []

        data = data_inicio
        contador = primeiro_dia
        for i in range(final):
            agend_manha = agendamentos.count((data, 'M'))
            agend_tarde = agendamentos.count((data, 'T'))
            data_formatada = data.strftime('%d-%m-%Y')

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
            elif data < hoje:
                semana.append({'data': data_formatada, 'status': 'desabilitado'})
            else:
                semana.append({'data': data_formatada, 'status': 'disponivel',
                               'motivo': {'manha': agend_manha, 'tarde': agend_tarde}})

            if i == final - 1 and contador % 7 != 5:
                dias.append(semana)
            data += incremento
            contador += 1
        self.context['calendario'] = dias
        return render(request, 'agendamento/calendario.html', self.context)


class Agendar(View):
    tamplete_name = 'agendamento/agendar.html'
    context = {}

    def get(self, request, **kargs):
        validar_data(kargs['data'])
        validar_profissional(kargs['profissional'])

        self.context['data'] = kargs['data'].replace('-', '/')
        self.context['turno'] = 'Manhã' if kargs['turno'] == 'M' else 'Tarde'
        self.context['profissional'] = 'Médico(a)' if kargs['profissional'] == 'med' else 'Enfermeiro(a)'
        return render(request, self.tamplete_name, self.context)

    def post(self, request, **kargs):
        validar_data(kargs['data'])
        profissional = kargs['profissional']
        validar_profissional(profissional)

        nome = request.POST.get('nome')
        paciente = Paciente.objetos.filter(nome=nome).last()
        if paciente is not None:
            data = kargs['data'].split('-')
            agendamento = Agendamento(
                paciente=paciente,
                profissional=kargs['profissional'],
                turno=kargs['turno'],
                data=f'{data[2]}-{data[1]}-{data[0]}'
            )
            agendamento.save()
            return redirect('agendamento:calendario', profissional=profissional, ano=data[2], mes=data[1])
        else:
            self.context['msg'] = f'O paciente {nome} não está cadastrado. Cadastre-o!'
            return render(request, self.tamplete_name, self.context)


class Agendados(View):
    template_name = 'agendamento/agendados.html'
    context = {}

    def get(self, request, **kargs):
        data = request.GET.get('data', None)
        #validar_data(data)

        profissional = kargs['profissional']
        validar_profissional(profissional)

        pacientes = Agendamento.objetos.filter(data=data, profissional=profissional).values('paciente','paciente__familia')
        self.context['manha'] = pacientes.filter(turno='M')
        self.context['tarde'] = pacientes.filter(turno='T')

        self.context['pacientes'] = pacientes
        return render(request, self.template_name, self.context)


def validar_data(data: str):
    """
    :param data: dd-mm-aaaa
    :return: retorna erro 404 se a data não existir
    """
    try:
        datetime.strptime(data, '%d-%m-%Y')
    except ValueError:
        raise Http404('Data Inválida')


def validar_profissional(profissional):
    if profissional not in ('med', 'enf'):
        raise Http404("profissional não existe")
