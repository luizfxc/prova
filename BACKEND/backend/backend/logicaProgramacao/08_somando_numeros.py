def somar_cinco_numeros():
    soma = 0
    for i in range(1, 6):
        numero = float(input(f"Digite o {i}º número: "))
        soma += numero
    print(f"A soma dos números é: {soma}")

somar_cinco_numeros()