# var1 = primeiro numero
# var2 = segundo numero
# soma = adicao
# sub = subtracao
# mult = multiplicacao
# div = divisao
# pot = potenciacao

operacao = input("Digite a operacao desejada (soma, sub, mult, div, pot): ")
var1 = float(input(''))
var2 = float(input(''))
if operacao == "soma":
	resultado = float(var1) + float(var2)
elif operacao == "sub":
	resultado = float(var1) - float(var2)
elif operacao == "mult":
	resultado = float(var1) * float(var2)
elif operacao == "div":
	resultado = float(var1) / float(var2)
elif operacao == "pot":
	resultado = float(var1) ** float(var2)
else:
	resultado = "Operação não suportada"
    
print("O resultado da operação é: " + str(resultado))
