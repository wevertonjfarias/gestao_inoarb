# Generated by Django 2.2.5 on 2019-10-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20191026_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Imagem'),
        ),
    ]