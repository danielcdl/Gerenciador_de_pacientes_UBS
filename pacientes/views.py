from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView

from pacientes.forms import PacienteForm
from pacientes.models import Paciente


class Consulta(TemplateView):
    template_name = "pacientes/consulta.html"


class Cadastro(View):
    template_name = 'pacientes/cadastro.html'
    context = {}

    def post(self, request):
        sus = self.request.POST.get('sus', '').strip()
        nome = self.request.POST.get('nome', '').lower().strip()
        paciente = None
        if sus:
            paciente = Paciente.objetos.filter(sus=sus).last()

        if sus == '' or paciente is None:
            paciente = Paciente.objetos.filter(nome__iexact=nome)

        if paciente:
            form = PacienteForm(request.POST, instance=paciente)
        else:
            form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()
            self.context['mensagem'] = 'Paciente cadastrado com sucesso'
            return HttpResponseRedirect(reverse_lazy('paciente:cadastro', self.context))
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)

    def get(self, request):
        form = PacienteForm(self.request.GET)
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class BuscarPacientes(View):
    template_name = 'pacientes/buscar.html'
    context = {}

    def get(self, request):
        pesquisar = self.request.GET.get('pesquisar', False)
        if pesquisar:
            tipo = self.request.GET.get('tipo')
            dado = self.request.GET.get('dado')

            pacientes = Paciente.objetos.all()
            if tipo and dado:
                if tipo == 'sus':
                    pacientes = pacientes.filter(sus=dado)
                elif tipo == 'mae':
                    pacientes = pacientes.order_by('mae').filter(mae__icontains=dado)
                elif tipo == 'nascimento':
                    pacientes = pacientes.filter(nascimento=dado)
                elif tipo == 'familia':
                    pacientes = pacientes.filter(familia=dado)
                else:
                    pacientes = pacientes.filter(nome__icontains=dado)
            self.context['pacientes'] = pacientes
        return render(request, self.template_name, self.context)


def consultar_paciente(request):
    if request.method == "GET":
        sus = request.GET.get('sus')
        nome = request.GET.get('nome')

        if sus:
            paciente = Paciente.objetos.filter(sus=sus).last()
        else:
            paciente = Paciente.objetos.filter(nome__iexact=nome).last()

        if paciente is not None:
            dados = {
                'sus': paciente.sus,
                'nome': paciente.nome,
                'mae': paciente.mae,
                'nascimento': paciente.nascimento,
                'familia': paciente.familia,
                'observacao': paciente.observacao,
                'encontrado': True
            }
        else:
            dados = {'encontrado': False}
        return JsonResponse(dados)
