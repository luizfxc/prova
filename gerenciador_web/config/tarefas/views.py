from django.shortcuts import render, get_object_or_404
from .models import Tarefa

# from .models import Tarefa
# from django.http import HttpResponse

# def listar_tarefas (request):
#     tarefas_salvas = Tarefa.objects.all()
#     print (tarefas_salvas)
#     return HttpResponse ("View 'listar_tarefas' executar! Confira no terminal")

def listar_tarefas(request):
    # 1: A busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()

    # 2. criamos um "dicionario de contexto" para enviar os dados ao template.
    # A chave 'minhas_tarefas' sera a variavel que usaremos no HTML.
    contexto = {
        'minhas_tarefas': tarefas_salvas
    }

    # 3. Renderizamos o template, passando a requisiçao e o contexto com os dados.
    return render(request, 'tarefas/lista.html', contexto)

def detalhe_tarefa(request, tarefa_id):
    # Busca uma tarefa pelo id 
    # Se nao encontrar retorna um erro 404
    tarefa = get_object_or_404 (Tarefa, pk= tarefa_id)
    return render (request, 'tarefas/detalhe.html', {'tarefa': tarefa})