import json

estoque_categoria = []
estoque_produto = []

id_categoria = 0
id_produto = 0

loja_generio = 'loja_generico.json'


def menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1) Cadastrar Categoria")
    print("2) Cadastrar Produto")
    print("3) Listar Produtos")
    print("4) Sair")


def cadastrar_categoria():
    global id_categoria
    print("\n--- Cadastro de Categoria ---")
    nome_categoria = input("Digite o nome da categoria: ")
    id_categoria += 1

    categoria = {
        "id_categoria": id_categoria,
        "nome_categoria": nome_categoria
    }

    estoque_categoria.append(categoria)
    print("Categoria cadastrada com sucesso!")


def cadastrar_produto():
    global id_produto

    if not estoque_categoria:
        print(" Nenhuma categoria cadastrada. Por favor, cadastre uma categoria primeiro.")
        return

    print("\n--- Categorias Disponíveis ---")
    for cat in estoque_categoria:
        print(f"  ID: {cat['id_categoria']} - Nome: {cat['nome_categoria']}")

    id_produto += 1
    nome_produto = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço do produto: "))
    id_categoria_associado = int(input("Informe o ID da categoria: "))

    produto = {
        "id_produto": id_produto,
        "nome_produto": nome_produto,
        "preco": preco,
        "id_categoria_associado": id_categoria_associado
    }

    estoque_produto.append(produto)
    print(" Produto cadastrado com sucesso!")


def listar_produtos():
    if not estoque_produto:
        print(" Nenhum produto cadastrado.")
        return

    print("\n--- Lista de Produtos Cadastrados ---")
    for produto in estoque_produto:
        nome_categoria_encontrado = "Categoria não encontrada"

        for categoria in estoque_categoria:
            if categoria["id_categoria"] == produto["id_categoria_associado"]:
                nome_categoria_encontrado = categoria["nome_categoria"]
                break

        print(f"\n Produto ID: {produto['id_produto']}")
        print(f"   Nome: {produto['nome_produto']}")
        print(f"   Preço: R$ {produto['preco']}")
        print(f"   Categoria: {nome_categoria_encontrado}")


def salvar_dados():
    dados = {
        "categorias": estoque_categoria,
        "produtos": estoque_produto
    }
    with open(loja_generio, 'w') as f:
        json.dump(dados, f, indent=4)
    print(" Dados salvos com sucesso!")


def carregar_dados():
    global estoque_categoria, estoque_produto, id_categoria, id_produto

    try:
        with open(loja_generio, 'r') as f:
            dados_carregados = json.load(f)
            estoque_categoria = dados_carregados.get("categorias", [])
            estoque_produto = dados_carregados.get("produtos", [])
            print(" Dados carregados com sucesso!\n")
    except FileNotFoundError:
        print(" Arquivo de dados não encontrado. Nenhum dado foi carregado.\n")
    except (json.JSONDecodeError, KeyError):
        print(" Erro ao ler o arquivo de dados.\n")

carregar_dados()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        cadastrar_produto()
    elif opcao == '3':
        listar_produtos()
    elif opcao == '4':
        salvar_dados()
        print("\n🚪 Encerrando o sistema... Até logo!")
        break
    else:
        print(" Opção inválida. Tente novamente.")
