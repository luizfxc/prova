import json
estoque_produto = []
estoque_categoria = []
id_produto = 0
id_categoria = 0 
categoria = 'categoria.json'
def carregar_arquivo(nome):
    try:
        with open(categoria,'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_arquivo(nome, dados):
    with open(nome, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def exibir_menu():
        print("----------loja generico-----------:")
        print("1.Cadastrar Categoria")
        print("2.Listar Categoria")
        print("3.Categoria Associada")
        print("4.Sair")

def cadastrar_categoria():
    global id_categoria
    print("\nCadastrar categoria")
    nome_categoria = input("Nome")
    id_categoria +=1

    categoria = {
        "id_categoria" : id_categoria,
        "nome_categoria" : nome_categoria
    }

    estoque_categoria.append(categoria)
    print(" Categoria salva ")

def cadastrar_produto():
    global id_produto

    if not estoque_categoria:
        print("Erro: Categoria não cadastrada. Cadastre uma categoria")
        return
    
    for cat in estoque_categoria:
        print(f"  ID: {cat['id_categoria']} - Nome: {cat['nome_categoria']}")

    id_produto += 1
    nome_produto = input("Nome: ")
    preco = int(input("Preço: "))
    id_categoria_associado = int(input("ID_categoria: "))

    produto = {
        "id_produto" : id_produto,
        "nome_produto" : nome_produto,
        "preco" : preco,
        "id_categoria_associado" : id_categoria_associado
    }

    estoque_categoria.append(produto)
    print(" Produto salvo ")

def listar_produtos():
    if not estoque_produto and estoque_categoria:
        print("\n Nenhum produto cadastrado")
        return

def listar_categoria():
    if not estoque_produto and estoque_categoria:
        print("\n Nenhum produto cadastrado")
        return


while True:
   exibir_menu()
   opcao = input("Escolha uma opção: ")

   if opcao == '1':
       cadastrar_categoria()
     elif opcao == '2':
       cadastrar_produto()
    elif opcao == '3':
       listar_produtos()
    elif opcao == '4':
       listar_categoria()
  
      