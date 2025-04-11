#Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

digite = str(input("Digite uma letra :"))


if digite == 'a' or digite == 'e' or digite == 'i' or digite == 'o' or digite == 'u':
    print(f"A letra que você digitou : {digite} é uma vogal")
else:
    print(f"A letra que você digitou : {digite} é uma consoante")