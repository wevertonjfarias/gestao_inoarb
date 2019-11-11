# Generated by Django 2.2.5 on 2019-10-22 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='cep',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='cpf',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='telefone',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
    ]