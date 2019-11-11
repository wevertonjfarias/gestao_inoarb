from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ocorrencia
from django.core.paginator import Paginator


@login_required
def listIndex(request):

    ocorrencia = Ocorrencia.objects.all().order_by('-data_ocorrencia')

    paginator = Paginator(ocorrencia, 8)

    page = request.GET.get('page')

    ocorrencia = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'ocorrencia': ocorrencia})


def dashboard(request):
    return render(request, 'tasks/dashboard.html')
