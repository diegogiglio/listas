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

#Remontando elementos com join
#objetivo = ["quero", "Ficar", "rico"]
#como = '$'.join(objetivo)
#print(como)

#Podemos colocar qualquer tipo de elemento em uma lista
'''lista6 = [1, 2, 3, 'Diego', [123, 456, 789]]
type(lista6)
print(lista6)'''

#Iterando em listas
''''
lista1 = [1, 2, 3, list('Diego'), [123, 456, 789]]
for elemento in lista1:
    print(elemento)
'''

#Somando elementos de uma lista com for
'''
lista2 = [10, 10, 10, 10, 10]
soma = 0
for _ in lista2:
    soma = _ + soma
    print(soma)
'''
'''
#somando elementos de uma lista com while
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista ou digite sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
'''
'''
#Utilizando variáveis em listas
numero = [1, 2, 3, 4, 5]
soma = 0
for _ in numero:
    soma = soma + _
print(soma)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numero = num1 + num2 + num3 + num4 + num5
print(numero)
'''
'''
#converter string em lista
#slipt transforma uma string em uma lista de elementos separados por padrão por espaço.
nome = 'Diego Aguilar Giglio'
nome = nome.split('i', 2)
print(nome)
'''
'''
#converter lista em string com join. O join concatena strings conforme o separador inicial
lista = list('diego')
nome = ''.join(lista)
print(nome)
'''
'''
#imprimindo variáveis através de índices
cores = ["Verde", "Amarelo", "Azul", "Branco"]
print(cores[1])
#para imprimir na ordem inversa utilize - (menos)
print(cores[-2])
'''
'''
#Encontrar determinado valor em uma lista
cores = ["Verde", "Amarelo", "Azul", "Branco"]
print(cores.index('Azul'))
'''

'''
#Procurando valores dentro de um intervalo
numeros = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0]
print(numeros.index(5, 5, 9))
'''

'''
#procurar a partir de um índice até outro índice (slicing)
numeros = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0]
print(numeros[3:6])

#procurar a partide de um índice até outro índice de passo em passo
print(numeros[0::2])
'''

'''
#procurar a partide de um índice até outro índice de passo em passo
numeros = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0]
print(numeros[0::2])
'''
'''
#Inverter valores em uma lista
nome = ["Diego", "Giglio"]
nome[0], nome[1] = nome[1], nome[0]
print(nome)
nome.reverse()
print(nome)
'''

'''
lista = ["Diego", "Giglio"]
print(max(lista))
print(min(lista))
print(len(lista))
numeros = [1 ,2, 3, 5, 8]
print(sum(numeros))
'''
'''
#Desempacotamento de lista
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1, num2, num3)
'''
'''
#Copia de lista (deep copy) #adições na lista cópia NÃO adicionam na lista original
lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
'''

'''
#Cópia de lista (Shallow copy) - adições na lista cópia adicionam na lista original
lista = [1, 2, 3]
print(lista)
nova = lista
nova.append(4)
print(lista)
print(nova)
'''
