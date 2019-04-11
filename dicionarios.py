"""
Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}
#print(type({}))
OBS: Sobre dicionários
    Chave e valor são separados por dois pontos 'chave:valor';
    Tanto chave como valor podem ser de qualquer tipo de dado;
    Podemos misturar tipos de dados

#criação de dicionários
#forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'paraguai'}

print(paises)
print(type(paises))

#forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

#Acessando elementos
'''
print(paises['br'])
print(paises['eua'])
print(paises['py'])
print(paises['ur']) #caso não exista o elemento, recebe o erro de key error
'''

#Acessando elementos forma recomendada
print(paises.get('br'))
print(paises.get('ru')) #caso não exista o elemento, usando o get para acessar o elemento não exibe erro

russia = paises.get('ru', 'Não Encontrado') #Podemos definir um valor padrão caso não encontre o elemento


#Podemos verificar se determinada chave se encontra em dicionário
print('br' in paises)
print('eua' in paises)
print('ru' in paises)
print('py' in paises)


if 'br' in paises:
    print(paises['br'])

#paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'paraguai'}

#Podemos utilizar qualquer tipo de dado(int, float, string, boolean), inclusive listas, tuplas dicionário, como chaves
#de dicionários

#Tuplas são interessantes de ser utilizadas em chaves de dicionário pois são imutáveis
localidade = {
    (123.1233, 32.2222): 'Escritório em Tókio',
    (11.111, 58.555): 'Escritório em Nova York',
    (11.111, 111.111): 'Escritório em São Paulo',
}
print(type(localidade))
print(localidade)

"""

#Adicionar em dicionário
receita = {'jan': 100, 'fev': 200, 'mar': 300}
#Forma 1
receita['abr'] = 400

print(receita)