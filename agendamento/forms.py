from django.forms import ModelForm

from .models import Agendamento


class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        exclude = '__all__'