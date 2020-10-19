'''
OPERADOR TERNARIO
'''
#SEM OPERADOR TERNARIO

# logged_user = False
#
# if logged_user:
#     msg = 'Usuario logado.'
# else:
#     msg = 'Usuario precisa logar.'
#
# print(msg)

#COM OPERADOR TERNARIO
# logged_user = True
# msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'
#
# print(msg)

idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Digite penas numeros!')
else:
    idade = int(idade)
    eh_maior = (idade >= 18)
    msg = 'maior de idade.' if eh_maior else 'Menor de idade.'

    print(msg)