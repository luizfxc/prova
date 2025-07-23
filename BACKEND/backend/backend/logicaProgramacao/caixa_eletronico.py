
soma_V = 0
valor = int(input("Digite um valor para somar (0 para parar): "))
while valor != 0:
    soma_V += valor
    valor = int(input("Digite um valor para somar (0 para parar): "))

print("A soma é:", soma_V)

soma_F = 0
valor = int(input("Digite um valor para subtrair (0 para parar): "))
while valor != 0:
    soma_F -= valor
    valor = int(input("Digite um valor para subtrair (0 para parar): "))

print("A subtração é:", soma_F)