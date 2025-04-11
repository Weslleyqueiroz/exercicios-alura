#3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
lista = [1,4,7,2,4]
#removi os itens com o clear
lista.clear()

print(lista)

#4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista2 = [4,2,7,4,1]
lista.extend(lista2)

#printando itens
print(lista)





#adicionar varios elementos no final -> lista.extend()
#remover um elemnto -> lista.remove()