# Generated by Django 4.1.3 on 2022-12-06 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proprietario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                (
                    "sexo",
                    models.CharField(
                        choices=[
                            ("F", "Feminino"),
                            ("M", "Masculino"),
                            ("N", "Nenhuma das opções"),
                        ],
                        max_length=1,
                    ),
                ),
                ("email", models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Carro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_proprietario", models.CharField(max_length=100)),
                ("nome", models.CharField(max_length=50)),
                (
                    "modelo",
                    models.IntegerField(
                        choices=[("H", "hatch"), ("S", "Sedan"), ("C", "Conversível")]
                    ),
                ),
                (
                    "cor",
                    models.IntegerField(
                        choices=[(1, "Amarelo"), (2, "Azul"), (3, "Cinza")]
                    ),
                ),
                (
                    "proprietario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lojacarford.proprietario",
                    ),
                ),
            ],
        ),
    ]
