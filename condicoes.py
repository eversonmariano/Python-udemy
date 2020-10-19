nome = input('Qual o seu nome? \n')
idade = int(input('Qual sua idade? \n'))

#limite para pegar emprestimo
id_menor = 20 #muito jovem
id_maior = 30 #passou da idade

if(idade >= id_menor and idade <= id_maior):
    print(f'{nome}, emprestimo liberado!')
else:
    print(f'{nome}, emprestimo negado!')

