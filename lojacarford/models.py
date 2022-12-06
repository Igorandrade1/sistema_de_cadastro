from django.db import models

# Create your models here.


class Proprietario(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    email = models.EmailField(max_length=100)


class Carro(models.Model):
    nome_proprietario = models.CharField(max_length=100, blank=False, null=False)
    nome = models.CharField(max_length=50, blank=False, null=False)

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

    modelo = models.IntegerField(choices=MODELO_CHOICES, blank=False)
    cor = models.IntegerField(choices=COR_CHOICES, blank=False)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)


