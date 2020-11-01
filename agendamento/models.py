from django.db.models import Model
from django.db.models import CharField
from django.db.models import DateField


class Agendamento(Model):
    paciente = CharField(max_length=100)
    profissional = CharField(max_length=3, choices=[('med', 'Médico(a)'), ('enf', 'enfermeiro(a)')])
    data = DateField()
    turno = CharField(max_length=5, choices=[('M', 'Manhã'), ('T', 'Tarde')])
