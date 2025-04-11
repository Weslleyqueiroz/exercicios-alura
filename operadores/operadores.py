#numero = int(input("Digite o primeiro valor numérico :"))
#numero1 = int(input("Digite o segundo valor numérico :"))

#resultado = numero + numero1
#print(f"O resultado da soma dos valores é : {resultado}")

#numero2 = int(input("Digite o primeiro valor numérico :"))
#numero3 = int(input("Digite o segundo valor numérico :"))
#numero4 = int(input("Digite o terceiro valor numérico :"))

#soma = numero2 + numero3 + numero4
#print(f"O resultado da soma é: {soma}")

#valor1 = int(input("Digite o valor para subtração :"))
#valor2 = int(input("Digite o valor para subtração :"))

#sub = valor1 - valor2

#print(f"O resultado da subtração é : {sub}")

#numerador = int(input("Digite o numerador :"))
#denominador = int(input("Digite o denominador : "))

#divisao = numerador/denominador

#print(f"O resultado da divisão é : {divisao}")

#numerico1 = int(input("Digite o operador :"))
#numerico2 = int(input("Digite o valor da potência :"))

#potencia = numerico1**numerico2
#print(f"O resultado da potencia do {numerico1} é : {potencia}")

#numerador1 = int(input("Digite o numerador1 :"))
#denominador1 = int(input("Digite o denominador :"))

#divisao1 = numerador1//denominador1
#if (divisao1 == 0):
    #print("O resultado não pode ser igual a 0")
#else:
   # print(f"O resultado da divisão é : {divisao1}")

#digite = int(input("Digite o primeiro valor : "))
#digite2 = int(input("Digite o segundo valor : "))
#mult = digite*digite2
#print(mult)


soma = 0

for i in range(3):
    nota = float(input(f"Digite as suas 3 notas {i+1}: "))
    soma += nota
   
media = soma/3
print(f"A sua média é : {media}")