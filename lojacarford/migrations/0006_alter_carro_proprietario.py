# Generated by Django 4.1.3 on 2022-12-06 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lojacarford", "0005_alter_carro_proprietario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carro",
            name="proprietario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="lojacarford.proprietario",
            ),
        ),
    ]
