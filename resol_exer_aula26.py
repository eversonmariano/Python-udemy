@@@@
"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou ímpar. Caso o usuário não digite um
número inteiro, informe que nao é inteiro.
"""
#SOLUÇÂO:

# num_int = input('Digite o num inteiro: ')
#
# if num_int.isdigit():
#     num_int = int(num_int)
#
#     if num_int % 2 == 0:
#         print(f'{num_int} é par!')
#     else:
#         print(f'{num_int} é impar!')
# else:
#     print('Isso não é um número e/ou não é inteiro!')


"""
Faça um programa que peça ao usuario e, 
baseando-se no horario descrito,exiba a saudação apropriada. 
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = input('Digite horário (0-23): ')
#
# if horario.isdigit():
#     horario = int(horario)
#
#     if horario < 0 or horario > 23:
#         print('Horário deve estar entre 0 e 23')
#     else:
#         if horario <= 11:
#             print('Bom dia!')
#         elif horario <= 17:
#             print('Boa tarde!')
#         else:
#             print('Boa noite!')
# else:
#     print('Por favor, digite um horário entre 0 e 23h!')


"""
Faça um programa que peça o primeiro nome do usuario. 
Se o nome tiver 4 letras ou menos, escreva: "Seu nome é curto"; 
se tiver entre  5 e 6 letras, escreva: "Seu nome é normal!;
Maior que 6, escreva: "Seu nome é muito grande!".
"""

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto!')
elif tamanho <=6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')
