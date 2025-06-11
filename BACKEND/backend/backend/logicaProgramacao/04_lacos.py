numeros = (10, 15, 22, 33, 42, 55, 60, 73, 88, 91, 100)

quantidade_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1

print(f"Quantidade de números pares: {quantidade_pares}")

valor=int(input("Digite um valor:"))

soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite um valor"))
    soma+valor
    print("Valor total da soma: ", soma)

print("Valor total da soma: ", soma)







senha = ""
while senha != "chupa":
    senha = input("Digite a senha:")
    print("Senha Incorreta.")

print("Acesso liberado")