# nome = input('Qual seu nome? ')
#
# print(nome or None or False or 0 or 'vc nao digitou nada!' or 'outra coisa')
#No exemplo abaixo, 'const' assume o valor da primeira variavel (e condição True) que encontrar e printa.


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'ell'

const = a or b or c or d or e or g or f
print(const)

