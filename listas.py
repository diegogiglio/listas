'''
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, 
com a diferença de serem DINAMICO e também de podermos colocar QUALQUER tipo de dado


'''
'''
lista = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'K', 'D', 'C', 'H']
lista3 = []
lista4 = list(range(11))
lista5 = list('Diego Giglio')

#Podemos checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num} ')
else:
    print(f'Não encontrei o número {num} ')    

#Podemos facilmente ordenar uma lista
lista = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista.sort()
print(lista)

#Podemos facilmente contar o numero de ocorrencia de um valor na lista
qtde = lista5.count('i')
print(qtde)
print(lista5.count('D'))

#Adicionar elementos em lista
'''
'''
Para adicionar elementos em listas, utilizamos a função append
Obs.: Com append nós só conseguimos adicionar 1 elemento por vez
'''
'''
print(lista)
lista.append(42)
print(lista)

lista.append([8, 3, 1]) #Adicionando uma lista dentro de uma outra lista
print(lista)
lista.extend([123, 45, 51]) #Adicionando itens a lista, obrigatoriamente deve ser mais de 1 item (iteráveis)
print(lista)

#Podemos inserir um novo elemento a lista, informando a posição do índice
lista5.insert(6, 'Aguilar')
print(lista5)
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
#Formas de unir duas listas
#lista1.extend(lista2)
#lista1 = lista1 + lista2
#print(lista1)

#Forma de invertar uma lista
#lista1.reverse()
#print(lista1)

#Forma de copiar uma lista
#lista1 = lista2.copy()
#print(lista1)

#Forma de contar elementos na lista
#print(lista1.__len__())
#print(len(lista1))

#remove e retorna um elemento da lista
#lista1.pop(0)
#print(lista1)

#Limpar os elementos de uma lista
#lista1.clear()
#print(lista1)

#Split separa os elementos pelo espaço entre eles ou separa pelo valor determinado
#nome = 'Diego Giglio'
#nome = 'Diego,Giglio'
#nome = nome.split(',')
#print(nome)

#remonta os elementos de uma lista
#nome = list('Diego Aguilar Giglio')
#print(nome)
#junto = ''.join(nome)
#print(junto)

objetivo = ["quero", "Ficar", "rico"]
como = '$'.join(objetivo)
print(como)