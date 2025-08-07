cadastro = input("Seja Bem-vindo crie sua conta:")
saldo = 0.0
opcao = ""
print(f"Olá, {cadastro}! Sua conta foi criada com sucesso, o seu saldo inicial é de R$ {saldo:.2f}")

while opcao != "4":
    print("\n--- Menu ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Listar saldo")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    match opcao:
        case "1":
            valor = float(input("Digite um valor para depositar: R$ "))
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        case "2":
            valor = float(input("Digite o valor para sacar: R$ "))
            if valor > saldo:
                print("Saldo insuficiente para essa operação.")
            else:
                saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

        case "3":
            print(f"Saldo atual: R$ {saldo:.2f}")

        case "4":
            print(f"\nObrigado por usar nosso sistema, {cadastro}. Até a próxima!")

        case _:
            print("Opção inválida. Tente novamente.")