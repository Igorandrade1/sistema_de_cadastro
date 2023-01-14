# Generated by Django 4.1.3 on 2022-12-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lojacarford", "0003_remove_carro_nome_proprietario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carro",
            name="cor",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Amarelo"), (2, "Azul"), (3, "Cinza")],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="carro",
            name="modelo",
            field=models.IntegerField(
                blank=True,
                choices=[("H", "hatch"), ("S", "Sedan"), ("C", "Conversível")],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="carro",
            name="nome_carro",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]