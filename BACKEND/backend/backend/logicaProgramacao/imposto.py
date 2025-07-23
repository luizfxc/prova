salario = float(input("Digite o seu salario: "))

salario_anual = salario * 12
print("salario anual: ", salario_anual)

if salario >= 5000:
    imposto_mensal = salario * 0.12  

elif salario >= 2000 and salario <= 4999:
    imposto_mensal = salario * 0.07
    
else:
     imposto_mensal = salario * 0.03

print("imposto mensal:", imposto_mensal)

imposto_anual = imposto_mensal * 12
print("imposto anual", imposto_anual)