from django.db import models

# Create your models here.


class Proprietario(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    hatch = 'H'
    Sedan = 'S'
    Conversivel = 'C'

    MODELO_CHOICES = (
        (hatch, 'hatch'),
        (Sedan, 'Sedan'),
        (Conversivel, 'Conversível'),
    )

    COR_CHOICES = (
        (1, 'Amarelo'),
        (2, 'Azul'),
        (3, 'Cinza'),
    )

    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    email = models.EmailField(max_length=100)
    nome_carro = models.CharField(max_length=50, blank=True)
    modelo = models.IntegerField(choices=MODELO_CHOICES, blank=True, null=True)
    cor = models.IntegerField(choices=COR_CHOICES, blank=True, null=True)




