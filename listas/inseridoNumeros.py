#5) Faça um programa que, ao inserir um número qualquer, 
#cria uma lista contendo todos os números primos entre 1 e o número digitado.

digitar = int(input("Digite um número qualquer para criar uma lista :"))

lista = []

for num in range(2, digitar + 1):
    # Verificar se o número é primo
    is_primo = True
    for i in range(2, num):
        if num % i == 0:
            is_primo = False
            break
    if is_primo:
        lista.append(num)
    