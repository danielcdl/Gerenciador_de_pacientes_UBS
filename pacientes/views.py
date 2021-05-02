from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic import View

import pandas as pd

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
                pacientes = pacientes.filter(familia__familia=dado)
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

    def get(self, request):
        self.context['form'] = PacienteForm()
        return render(request, self.template_name, self.context)

    def post(self, request):
        n_familia = request.POST.get('familia')
        familia = get_object_or_404(Familia, familia=n_familia)
        chave = self.request.POST.get('chave', '')
        
        print(n_familia)
        print(familia)
        print(familia.id)
        print(chave)

        if chave:
            paciente = Paciente.objetos.filter(id=chave).last()
        else:
            paciente = None

        if paciente is not None:
            form = self.form_class(request.POST, instance=paciente)
        else:
            form = self.form_class(request.POST)

        if form.is_valid():
            form_paciente = form.save(commit=False)
            form_paciente.familia = familia.id
            form_paciente.save()
            return redirect('pacientes:cadastro_paciente')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class CadastroFamilia(View):
    template_name = 'pacientes/cadastro_familia.html'
    context = {}
    form_class = FamiliaForm

    def post(self, request):
        print(request.POST)
        chave = request.POST.get('chave', '')
        familia = None
        if chave:
            familia = Familia.objetos.filter(id=chave).last()
        else:
            familia = None

        if familia is not None:
            form = self.form_class(request.POST, instance=familia).last()
        else:
            form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pacientes:cadastro_paciente')
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

        if tipo == 'familia':
            dados = Familia.objetos.filter(familia=dado).values().last()
        else:
            if tipo == 'sus':
                dados = Paciente.objetos.filter(sus=dado).values().last()
            elif tipo == 'nome':
                dados = Paciente.objetos.filter(nome__iexact=dado).values().last()
            else:
                raise Http404('Tipo não encontrado')
            
            if dados is not None:
                dados['familia'] = Familia.objetos.filter(id=dados['familia_id']).last().familia
                print(Familia.objetos.filter(id=dados['familia_id']).last().familia)
            

        if dados is not None:
            dados = dict(dados)
            dados['encontrado'] = True
        else:
            dados = {'encontrado': False}
        print(dados)
        return JsonResponse(dados)

def consultar_familia(request, tipo, dado):

    if request.method == "POST":

        if tipo == 'sus':
            dados = Paciente.objetos.filter(sus=dado).values().last()
        elif tipo == 'nome':
            dados = Paciente.objetos.filter(nome__iexact=dado).values().last()
        else:
            raise Http404('Tipo não encontrado')

        if dados is not None:
            dados = dict(dados)
            dados['encontrado'] = True
        else:
            dados = {'encontrado': False}
        print(dados)
        return JsonResponse(dados)


def autocomplete_pacientes(request, **kargs):
    if request.method == "GET":
        nome = kargs['nome']
        pacientes = Paciente.objetos.filter(nome__istartswith=nome).values_list('id', 'nome')[:5]
        return JsonResponse(dict(pacientes))


def adicionar_pacientes_xls(request):
    if request.method == 'POST':
        dados = pd.read_excel("/relatorio.xls", sheet_name="Sheet0")
        for linha in dados:
            print(linha)
    return render(request, "pacientes/inserir_xls.html")