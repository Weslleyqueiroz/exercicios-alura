#incrementação em py
#cont = 1
#while cont <=10:
#    print(cont)
#    cont = cont+1

#for i in range(1,11):
#   print(i)


#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
#numero1 = int(input("Digite um número inteiro : "))
#numero2 = int(input("Digite um número inteiro : "))
#for i in range (numero1,numero2): 
#   print(i)

#coloniaA = 4
#coloniaB = 10

#taxa_A = 0.4
#taxa_B = 0.10

#dias = 0

#while coloniaA< coloniaB:
#    coloniaA += coloniaA * taxa_A
#    coloniaB +=coloniaB * taxa_B
#    dias = dias+1

#    print(f"A taxa de crescimento será em {dias}")

#cont = 0

#while cont <= 15:
#    nota = int(input("Digite uma nota de 0 a 5 : "))
#    if nota >5:
#        print("Nota valida")
#        cont = cont+1
#    else: 
#        print("Nota invalida, tente novamente")

#6) Escreva um programa que gere a tabuada 
#de um número inteiro de 1 a 10, de acordo com 
#a escolha da pessoa usuária. Como exemplo, para o 
#número 2, a tabuada deve ser mostrada no seguinte formato:

numero = int(input("Digite o número que será gerado a taboada :"))

while 1 <= numero <= 10:
    print(f"tabuada do : {numero}")
    for i in range(1,11):
        print(f'{numero} x {i} = {numero*i}')
    
    numero = int(input("\nDigite outro número (entre 1 e 10) para ver outra tabuada ou qualquer outro número para sair: "))

print("Digite um número válido (entre 1 e 10) da próxima vez!")