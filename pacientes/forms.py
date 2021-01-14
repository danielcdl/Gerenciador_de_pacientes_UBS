from django import forms

from .models import Paciente
from .models import Familia


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ('familia',)


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'