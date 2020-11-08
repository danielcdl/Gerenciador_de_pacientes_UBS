from django.db.models import Model
from django.db.models import CharField
from django.db.models import PositiveIntegerField
from django.db.models import DateField
from django.db.models import TextField
from django.db.models import ForeignKey
from django.db.models import SET_NULL
from django.db.models import Manager


class Paciente(Model):
    sus = CharField(
        max_length=18,
        blank=True,
        null=True,
    )

    nome = CharField(
        max_length=100,
        unique=True
    )

    mae = CharField(
        max_length=100,
        null=False,
        blank=True
    )

    nascimento = DateField(
        blank=True,
        null=True
    )

    familia = ForeignKey(
        'Familia',
        on_delete=SET_NULL,
        null=True,
        blank=True
    )

    observacao = TextField(
        max_length=255,
        blank=True
    )

    objetos = Manager()

    class Meta:
        ordering = ['nome']


class Familia(Model):
    familia = PositiveIntegerField()

    tipo_logradouro = CharField(
        max_length=100,
        null=True,
        blank=True
    )

    nome_logradouro = CharField(
        max_length=100,
        null=True,
        blank=True
    )

    numero = PositiveIntegerField(
        null=True,
        blank=True
    )

    bairro = CharField(
        max_length=100,
        null=True,
        blank=True
    )

    complemento = CharField(
        max_length=100,
        null=True,
        blank=True
    )

    cidade = CharField(
        max_length=100,
        null=True,
        blank=True
    )

    objetos = Manager()

    class Meta:
        ordering = ['familia']
