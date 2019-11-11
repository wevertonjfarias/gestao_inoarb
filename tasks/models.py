from django.db import models


class Ocorrencia(models.Model):

    TIPO = (
        ('QUEDA DE ARVORE', 'QUEDA DE ARVORE'),

    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', blank='True', max_length=100)
    cpf = models.CharField('CPF', max_length=15)
    endereco = models.CharField('endereço', blank='True', max_length=100)
    cidade = models.CharField('Cidade', blank='True', max_length=100)
    cep = models.CharField('CEP', max_length=30,  blank='True')
    telefone = models.CharField('Telefone', max_length=20, blank='True')
    data_ocorrencia = models.DateTimeField('Criado em', auto_now_add=True)
    tipo_ocorrencia = models.CharField(
        max_length=20,
        choices=TIPO,
    )
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    image = models.ImageField(upload_to='tmp', verbose_name='Imagem',
                              null=True, blank=True)

    def __str__(self):
        return self.endereco



