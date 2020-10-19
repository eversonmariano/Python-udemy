# WHILE SIGNIFICA ENQUANTO

# while True:
#     nome = input('Qual o seu nome? ')
#     print(f'Ola {nome}!')
#     break
# print('cabou!')

# x = 0
# while x < 10:
#     if x == 3:
#         x += 1
#         continue
#     print(x)
#     x += 1
# print('cabou!')

x = 0 #Coluna
y = 0 #Linha

# while x < 5:
#     y = 0
#     while y < 5:
#
#         print(f'({x},{y})')
#         y += 1
#     x += 1
#
# print('cabou!')


while True:
    sair = input('Deseja sair? [s] OU [n] ')
    if sair == 's':
        break
    #continue
    print()#pula uma linha
    n1 = input('Digite um num: ')
    n2 = input('Digite outro num: ')



    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um numero!')
        continue

    operador = input('Digite um operador: ')

    x += 1
    # + - / *
    n1 = float(n1)
    n2 = float(n2)
    if operador == '+':
        print(f'A soma é: {n1 + n2}')
    elif operador == '-':
        print(f'A subtraçao é: {n1 - n2}')
    elif operador == '/' and n2 != '0':
        print(f'A divisão é: {n1 / n2}')
    else:
        print(f'A multiplicaçao é: {n1 * n2}')

print('cabou!')



















