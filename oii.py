# print("oi 123 123 546 \n")
#
# nome = input("Qual é o seu nome? \n")
# idade = input("Qual sua idade? \n")
#
# print(f'Meu nome é {nome} e tenho {idade} anos.')
#
# n1 = int(input('Digite um numero: \n'))
# n2 = int(input('Digite o prox numero: \n'))
#
# print(f'Soma: {n1+n2}\n'
#       f'Multiplicão: {n1*n2}\n'
#       f'Divisão: {n1/n2}\n'
#       f'Subtração: {n1-n2}')

pi = 3.1415926535
a = float(pi)
print('%.2f'% a)
print(round(a, 3))#arredonda
print('O valor de pi formatado é {:.4f}'.format(pi))
print('{:.5f}'.format(pi))#trunca

print('{:.1f}'.format(pi))
print(round(pi,1))

nome = 'ell'
sobrenome = 'mariano'

print('{1}'.format(nome, sobrenome))#pega o valor pelo indice da variavel
print('{0}'.format(nome, sobrenome))#pega o valor pelo indice da variavel


print(nome.lower())#tudo minuscula
print(nome.upper())#tudo maiuscula
print(nome.title())#primeira letra MAIUSCULA
print(len(sobrenome))#conta caracters