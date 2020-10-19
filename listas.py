"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# lista = ['a','b','c','d','e',47, 'boi',52]
# print(len(lista))
# print(lista)
# print(lista[::-1])
# print(lista[2::])
# print(lista[:2:])
# print(lista[::2])
# l1 = [1,2,3]
# l2 = [4,5,6]
# #l3 = l1 + l2
# #l1.extend('r')
# #l2.append('t')
# l2.insert(0, 'banana')
# print(l2)
# l2.pop()
# print(l2)
# print(l1[3])
# print(l1)
#print(l3)
# l1.insert(0,'banana')
# print(l1)
# del(l1[3:5])
# print(l1)
# l1 = [1,2,3,4,5,6,7,8,9]
# print(max(l1))
# print(min(l1))
#l1 = list(range(0,20,2))
#
# l1 = [1,2,3,4,5,6,7,8,9]
# soma = 0
# for valor in l1:
#     soma = soma + valor
# print(soma)

'''
split, join, enumerate em PYTHON, FUNÇOES:
*SPLIT - DIVIDIR UMA STRING # STR
*JOIN - JUNTAR UMA LISTA #STR
*ENUMERATE - ENUMERAR ELEMENTOS DA LISTA #ITERAVEIS
'''

# string = 'O Brasil é o país do futebol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')

# for valor in lista_1:
#     print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase')

# palavra = ''
# cont = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > cont:
#         cont = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({cont}x)')

# frase = 'O Brasil é penta'
# print(frase)
# lista = frase.split(' ')
# print(lista)
# frase2 = '-'.join(lista)
# print(frase2)
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

#desempacotamento de lista em python
#lista = ['ell','maria','beta']
# for indice, nome in enumerate(lista):
#     print(indice, nome)

#desempacotamento de lista em python
# lista = ['ell','maria','beta',1,2,3,100]
# n1, n2, n3, *outra_lista, ultimo_daLista = lista
#
# print(ultimo_daLista)

#trocando o valor das variaveis em python

x = 10
y = 'ell'
#print(f'x={x} e y={y}')
#x, y = y, x
z = 'beta'
x, y, z = z, x, y
print(f'x={x} e y={y} e z={z}')












