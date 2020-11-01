from django.db.models import Model
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import Manager


class Agendamento(Model):
    paciente = CharField(max_length=100)
    profissional = CharField(max_length=3, choices=[('med', 'Médico(a)'), ('enf', 'enfermeiro(a)')])
    data = DateField()
    turno = CharField(max_length=5, choices=[('M', 'Manhã'), ('T', 'Tarde')])

    objetos = Manager()


class Feriado(Model):
    feriado = CharField(max_length=100)
    data = DateField()

    objetos = Manager()


class DiaIndisponivel(Model):
    motivo = CharField(max_length=100)
    profissional = CharField(max_length=3, choices=[('med', 'Médico(a)'), ('enf', 'enfermeiro(a)')])
    data = DateField()

    objetos = Manager()
