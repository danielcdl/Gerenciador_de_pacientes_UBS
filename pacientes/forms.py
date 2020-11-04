from django import forms

from .models import Paciente
from .models import Familia


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'