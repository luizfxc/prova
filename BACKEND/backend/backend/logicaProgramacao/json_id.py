# Sistema de Controle de Estoque - Moya's Imports

estoque = []

def exibir_menu():
    print("     Moya's Imports - Estoque de Veículos")
    print("1. Cadastrar veículo")
    print("2. Alterar veículo")
    print("3. Excluir veículo")
    print("4. Listar veículos")
    print("5. Sair")

def cadastrar_veiculo():
    print("\nCadastro de Novo Veículo:")
    nome = input("Nome: ")
    ano = input("Ano: ")
    km = input("Quilometragem: ")
    marca = input("Marca: ")
    preco = input("Preço (R$): ")
    cor = input("Cor: ")
    quantidade = input("Quantidade em estoque: ")

    veiculo = {
        "nome": nome,
        "ano": ano,
        "km": km,
        "marca": marca,
        "preco": preco,
        "cor": cor,
        "quantidade": quantidade
    }

    estoque.append(veiculo)
    print(" Veículo cadastrado com sucesso!")

def listar_veiculos():
    if not estoque:
        print("\n Nenhum veículo cadastrado.")
        return
    
    print("\nLista de Veículos no Estoque:")
    for i, v in enumerate(estoque):
        print(f"\nVeículo {i+1}:")
        for chave, valor in v.items():
            print(f"  {chave.capitalize()}: {valor}")

def alterar_veiculo():
    listar_veiculos()
    if not estoque:
        return

    try:
        idx = int(input("\nDigite o número do veículo que deseja alterar: ")) - 1
        if 0 <= idx < len(estoque):
            print("\nDigite os novos dados (aperte Enter para manter o atual):")
            veiculo = estoque[idx]
            for campo in veiculo:
                novo_valor = input(f"{campo.capitalize()} ({veiculo[campo]}): ")
                if novo_valor:
                    veiculo[campo] = novo_valor
            print(" Veículo atualizado com sucesso!")
        else:
            print(" Veículo não encontrado.")
    except ValueError:
        print(" Entrada inválida.")

def excluir_veiculo():
    listar_veiculos()
    if not estoque:
        return

    try:
        idx = int(input("\nDigite o número do veículo que deseja excluir: ")) - 1
        if 0 <= idx < len(estoque):
            confirmacao = input(f"Tem certeza que deseja excluir '{estoque[idx]['nome']}'? (s/n): ").lower()
            if confirmacao == 's':
                del estoque[idx]
                print(" Veículo excluído com sucesso!")
            else:
                print(" Exclusão cancelada.")
        else:
            print(" Veículo não encontrado.")
    except ValueError:
        print(" Entrada inválida.")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_veiculo()
    elif opcao == '2':
        alterar_veiculo()
    elif opcao == '3':
        excluir_veiculo()
    elif opcao == '4':
        listar_veiculos()
    elif opcao == '5':
        print("Encerrando sistema. Até logo!")
        break
    else:
        print(" Opção inválida. Tente novamente.")
