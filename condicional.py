#numero1 = int(input("Digite o primeiro número :"))
#numero2 = int(input("Digite o segundo número :"))

#if numero1 > numero2:
 #   print(f"O numero {numero1} é maior que o {numero2}")
#else:
#    print(f"o numero {numero2} é maior.")

#percentual = float(input("Digite o percentual de crescimento :"))

#if percentual >0 :
   # print("O percentual é positivo!")
#elif percentual<0:
   # print("O percentual é negativo!")
#else:
   # print("O percentual é estavel!")

numero1 = int(input("Digite o primeiro numero :"))
numero2 = int(input("Digite o segundo numero :"))
print("Qual operação você deseja realizar? ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacoes = input("Digite o número desejado para escolher : ")

if operacoes == "1":
    resultado = numero1 + numero2
elif operacoes == "2":    
    resultado = numero1 - numero2
elif operacoes == "3":
    resultado = numero1 * numero2
else:
    resultado = numero1/numero2

if resultado %2 ==0:
      par_ou_impar = "par"
else:
      par_ou_impar = "ímpar"

if resultado > 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"
else:
    sinal = "zero (neutro)"

if resultado == int(resultado):
    tipo = "inteiro"
else:
    tipo = "decimal"

print(f" O resultado é {resultado}")
print(f"O numero é {par_ou_impar}, {sinal} e {tipo}")

