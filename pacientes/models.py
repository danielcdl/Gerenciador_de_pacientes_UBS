from django.db.models import Model
from django.db.models import CharField
from django.db.models import PositiveIntegerField
from django.db.models import DateField
from django.db.models import TextField
from django.db.models import Manager


class Paciente(Model):
    sus = CharField(
        max_length=18,
        blank=True,
        null=True,
        unique=True
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

    familia = PositiveIntegerField(
        null=True,
        blank=True
    )

    observacao = TextField(
        max_length=255,
        blank=True
    )

    tipo_logradouro = CharField(
        max_length=100,
        null=False,
        blank=True
    )

    nome_logradouro = CharField(
        max_length=100,
        null=False,
        blank=True
    )

    numero = PositiveIntegerField(
        null=True,
        blank=True
    )

    bairro = CharField(
        max_length=100,
        null=False,
        blank=True
    )

    complemento = CharField(
        max_length=100,
        null=False,
        blank=True
    )

    cidade = CharField(
        max_length=100,
        null=False,
        blank=True
    )

    objetos = Manager()

    class Meta:
        ordering = ['nome']
