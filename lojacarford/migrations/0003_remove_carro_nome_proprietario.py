# Generated by Django 4.1.3 on 2022-12-06 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lojacarford", "0002_rename_nome_carro_nome_carro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carro",
            name="nome_proprietario",
        ),
    ]
