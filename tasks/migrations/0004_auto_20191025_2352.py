# Generated by Django 2.2.5 on 2019-10-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20191024_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='cep',
            field=models.DecimalField(blank='True', decimal_places=0, max_digits=20),
        ),
    ]
