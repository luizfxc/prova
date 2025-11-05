from django.shortcuts import render, get_object_or_404, redirect

from projetos.models import Projeto
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

def adicionar_tarefa(request):
        projetos = Projeto.objects.all()
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            projeto_id = request.POST.get('projeto')
            projeto_selecionado = Projeto.objects.get (pk = projeto_id)
            Tarefa.objects.create(titulo=titulo, descricao=descricao, projeto = projeto_selecionado)
        return redirect('listar_tarefas')
        return  render (request,'tarefas/form_tarefa.html', {'projetos':projetos})

def alterar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto')
        concluida = request.POST.get('concluida') == 'on' 

        projeto_selecionado = get_object_or_404 (Projeto, pk = projeto_id)

      
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluida = concluida
        tarefa.projeto = projeto_selecionado

        tarefa.save()
        
        return redirect('listar_tarefas')

    context = {
        'tarefa': tarefa,
        'projetos': projetos,
    }
    return render(request, 'tarefas/form_tarefa.html', context)

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk = tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar_tarefas')
    return render (request,'tarefas/confirmar_exclusao.html',{'tarefa':tarefa})

    
    #métodos http

    #POST: envia dados para o servidor

    #GET: busca dados no servidor

    #PUT: atualiza recursos existentes

    #DELETE: remove recursos selecionados