# Generated by Django 2.2.5 on 2019-10-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.DecimalField(decimal_places=2, max_digits=12)),
                ('geolocalidade', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('cep', models.DecimalField(decimal_places=2, max_digits=20)),
                ('telefone', models.DecimalField(decimal_places=2, max_digits=20)),
                ('data_ocorrencia', models.DateTimeField(auto_now_add=True)),
                ('tipo_ocorrencia', models.CharField(choices=[('QUEDA DE ARVORE', 'QUEDA DE ARVORE')], max_length=20)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
