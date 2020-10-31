from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView

from pacientes.forms import PacienteForm
from pacientes.models import Paciente


class Consultar(TemplateView):
    template_name = "pacientes/consultar.html"


class Cadastro(View):
    template_name = 'pacientes/cadastro.html'
    context = {}
    form_class = PacienteForm

    def post(self, request):
        sus = self.request.POST.get('sus', '').strip()
        nome = self.request.POST.get('nome', '').lower().strip()
        paciente = None
        mensagem = {}
        if sus:
            paciente = Paciente.objetos.filter(sus=sus).last()

        if sus == '' or paciente is None:
            paciente = Paciente.objetos.filter(nome__iexact=nome)

        if paciente:
            form = self.form_class(request.POST, instance=paciente)
        else:
            form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            mensagem['sucesso'] = 'Paciente cadastrado com sucesso'
            return render(request,'pacientes/cadastro.html', {'mensagem': mensagem})
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context,)

    def get(self, request):
        form = PacienteForm(self.request.GET)
        self.context['form'] = form
        return render(request, self.template_name, self.context)


def tabela_busca(request):
    tipo = request.GET.get('tipo')
    dado = request.GET.get('dado')
    pacientes = Paciente.objetos.all()

    if tipo != '' and dado != '':
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
    return render(request, 'pacientes/tabela_busca.html', {'pacientes': pacientes})


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
