from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Ocorrencia


class TaskAdmin(admin.ModelAdmin):

    list_display = ['endereco', 'nome', 'cidade', 'tipo_ocorrencia', 'data_ocorrencia']
    search_fields = ['nome', 'data_ocorrencia']


admin.site.register(Ocorrencia, TaskAdmin)

admin.site.site_header = 'Administração INOARB'

admin.site.index_title = 'InoArb - Gestão em Arborização | Admin'
