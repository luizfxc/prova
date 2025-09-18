from django.shortcuts import render

from .models import Tarefa

from django.http import HttpResponse

def listar_tarefas(request):
    tarefa_salvas = Tarefa.objects.all()
    print(tarefa_salvas)
    return HttpResponse("View 'listar_tarefas' executada! Confira no terminal")
