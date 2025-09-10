import json
produto = []
categoria = []
id_produto = 1
id_categoria = 2

def cadastrar_categoria():
    try:
        with open('categorias.json','r') as arquivo:
            categoria = json.load (arquivo)
            print ("arquivo carregado!")
    except FileNotFoundError:
        print("arquivo categorias.json arquivo não encontrado")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo")
            
def salvar_arquivo():
    with open(categoria,'w') as arquivo:
        json.dump(arquivo, indent=4)
    print("Arquivo salvo com sucesso")

def exibir_menu():
    print("----------loja generico-----------:")
    print("1.Cadastrar Categoria")
    print("2.Listar Categoria")
    print("3.Categoria Associada")
    print("4.Sair")

def cadastrar_categoria():
    nome = input("Nome da nova categoria: ")
    


    