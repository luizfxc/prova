from django.shortcuts import render, get_object_or_404, redirect
from .models import Projeto

# from .models import Tarefa
# from django.http import HttpResponse

# def listar_tarefas (request):
#     tarefas_salvas = Tarefa.objects.all()
#     print (tarefas_salvas)
#     return HttpResponse ("View 'listar_tarefas' executar! Confira no terminal")

def listar_projetos(request):
    # 1: A busca no banco de dados continua a mesma
    projetos_salvos = Projeto.objects.all()

    # 2. criamos um "dicionario de contexto" para enviar os dados ao template.
    # A chave 'minhas_tarefas' sera a variavel que usaremos no HTML.
    contexto = {
        'meus_projetos': projetos_salvos
    }

    # 3. Renderizamos o template, passando a requisiçao e o contexto com os dados.
    return render(request, 'projetos/lista.html', contexto)

