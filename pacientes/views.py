from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic import View

from pacientes.forms import PacienteForm
from pacientes.forms import FamiliaForm
from pacientes.models import Paciente
from pacientes.models import Familia


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


class Cadastro(TemplateView):
    template_name = 'pacientes/cadastro.html'


class CadastroPaciente(View):
    template_name = 'pacientes/cadastro_paciente.html'
    context = {}
    form_class = PacienteForm

    def post(self, request):
        sus = self.request.POST.get('sus', '').strip()
        nome = self.request.POST.get('nome', '').lower().strip()
        paciente = None

        if sus != '':
            paciente = Paciente.objetos.filter(sus=sus).last()

        if sus == '' or paciente is None:
            paciente = Paciente.objetos.filter(nome__iexact=nome).last()

        if paciente is not None:
            form = self.form_class(request.POST, instance=paciente)
        else:
            form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pacientes:cadastro_paciente')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context, )

    def get(self, request):
        form = PacienteForm(self.request.GET)
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class CadastroFamilia(View):
    template_name = 'pacientes/cadastro_familia.html'
    context = {}
    form_class = FamiliaForm

    def post(self, request):
        n_familia = request.POST.get('familia')
        familia = Familia.objetos.filter(familia=n_familia).last()

        if familia is not None:
            form = self.form_class(request.POST, instance=familia)
        else:
            form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pacientes:paciente_cadastro')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)

    def get(self, request):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)


def consultar_paciente(request, **kargs):
    if request.method == "GET":
        tipo = kargs['tipo']
        dado = kargs['dado']

        if tipo == 'sus':
            dados = Paciente.objetos.filter(sus=dado).values().last()
        elif tipo == 'nome':
            dados = Paciente.objetos.filter(nome__iexact=dado).values().last()
        elif tipo == 'familia':
            dados = Familia.objetos.filter(familia=dado).values().last()
        else:
            raise Http404('Tipo não encontrado')

        if dados is not None:
            dados = dict(dados)
            dados['encontrado'] = True
        else:
            dados = {'encontrado': False}
        return JsonResponse(dados)


def autocomplete_pacientes(request, **kargs):
    if request.method == "GET":
        nome = kargs['nome']
        pacientes = Paciente.objetos.filter(nome__istartswith=nome).values_list('id', 'nome')[:5]
        return JsonResponse(dict(pacientes))
