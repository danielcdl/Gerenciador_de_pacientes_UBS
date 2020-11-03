from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View

from pacientes.forms import PacienteForm
from pacientes.models import Paciente


class Consultar(View):
    template_name = "pacientes/consultar.html"

    def get(self, request):
        tipo = request.GET.get('tipo', '')
        dado = request.GET.get('dado', '')
        pagina = request.GET.get('pagina')
        pacientes = Paciente.objetos.all()
        paginado = False
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
        else:
            paginacao = Paginator(pacientes, 10)
            pacientes = paginacao.get_page(pagina)
            paginado = True
        return render(request, self.template_name, {'pacientes': pacientes, 'paginado': paginado})


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
            return render(request, 'pacientes/cadastro.html', {'mensagem': mensagem})
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context, )

    def get(self, request):
        form = PacienteForm(self.request.GET)
        self.context['form'] = form
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


def autocomplete_pacientes(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        pacientes = Paciente.objetos.filter(nome__istartswith=nome).values_list('id', 'nome')[:5]
        return JsonResponse(dict(pacientes))
