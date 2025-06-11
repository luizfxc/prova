
def saudacao(nome):
   return print(f"Olá, {nome}")

def calcular_media(a, b):
    return print (a + b) / 2


def eh_par(numero):
    return numero % 2 == 0

print(saudacao("luiz gosotoso"))

print(calcular_media(777,98))

def parouimpar(numero):
    if (numero % 2 == 0):
        return print("O numero é par")
    else:
        return print("O valor é impar")
    
    print(parouimpar(20))
    