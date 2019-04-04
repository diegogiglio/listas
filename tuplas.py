'''
Tuplas (tupla)
Tuplas são bastante parecidas com listas.
Existem basicamente suas diferenças básicas:

1) As tuplas são representadas por parênteses ()

2) As tuplas são imutáveis, isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.


'''
'''
#As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#Cuidado 2: tuplas com 1 elemento

tupla3 = (4) #Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) #isso é uma tupla. Logo podemos concluir que a dupla é definida pela virgula (,) e não pelo uso do parênteses
print(tupla4)
print(type(tupla4))

tupla5 = tupla4
tupla5 = tupla4 + tupla2
print(tupla5 [-2])
print(type(tupla5))
'''
'''
tupla = tuple(range(11))
print(tupla)
'''
'''
tupla = 'Diego', 'Aguilar', 'Giglio'
nome, sobrenome1, sobrenome2 = tupla
print(nome)
print(sobrenome1)
print(sobrenome2)
print(f'{sobrenome2} {sobrenome1} {nome}')
'''
'''
tupla = ('Diego', 1, 2, 3, 'Giglio') # A tupla tb suporta varios tipos de arquivos
print(tupla)
'''
'''
#Soma, valor maximo, minimo, tamanho
tupla = (1, 2, 3, 4, 5)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
'''
'''
tupla = (1, 2, 3, 4, 5, 'Diego')
#print('Diego' in tupla)
for n in tupla:
    print(n)

for indice in enumerate(tupla):
    print(indice)

'''
'''
tupla = (1, 2, 3, 4, 5, 'Diego', 'Diego', 'Diego') #contando quantos elementos existem na tupla
print(tupla.count('Diego'))

nome = tuple('diego aguilar giglio')
print(nome)
'''
#As tuplas devem ser usadas sempre que não houver necessidade de mudar os elementos
#meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
#print(meses.__sizeof__()) #checando tamanho (em bytes) da tupla
'''
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1
'''
#print(meses.index('Abril', 2))
#print(meses[0:5:2]) #slicing é pegar valores de fatia em fatia

help(format)