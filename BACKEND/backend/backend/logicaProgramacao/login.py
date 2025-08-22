def adicionar():
    try:
        nome = input("Nome: ")
        with open("usuarios.txt", "a") as f:
            f.write(nome + "\n")
        print("Usuário adicionado.")
    except:
        print("Erro ao adicionar.")

def listar():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines()
        for i, u in enumerate(usuarios):
            print(f"{i + 1}. {u.strip()}")
    except:
        print("Nenhum usuário cadastrado.")

def alterar():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines()
        listar()
        i = int(input("Número do usuário para alterar: ")) - 1
        novo = input("Novo nome: ")
        usuarios[i] = novo + "\n"
        with open("usuarios.txt", "w") as f:
            f.writelines(usuarios)
        print("Usuário alterado.")
    except:
        print("Erro ao alterar.")

def excluir():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines()
        listar()
        i = int(input("Número do usuário para excluir: ")) - 1
        usuarios.pop(i)
        with open("usuarios.txt", "w") as f:
            f.writelines(usuarios)
        print("Usuário excluído.")
    except:
        print("Erro ao excluir.")

def menu():
    while True:
        print("\n1. Adicionar\n2. Listar\n3. Alterar\n4. Excluir\n5. Sair")
        op = input("Escolha: ")
        if op == "1":
            adicionar()
        elif op == "2":
            listar()
        elif op == "3":
            alterar()
        elif op == "4":
            excluir()
        elif op == "5":
            break
        else:
            print("Opção inválida.")

menu()