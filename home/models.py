from django.db.models import Model
from django.db.models import CharField
from django.db.models import ImageField
from django.db.models import PositiveIntegerField


class Posto(Model):
    #logo = ImageField()

    nome = CharField(
        max_length=100
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
