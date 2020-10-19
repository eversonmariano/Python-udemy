
frase = 'o rato roeu '
#'a roupa do rei de roma'
tam_frase = len(frase)
# indices de a a 33
cont = 0
nova_string = ''

while cont < tam_frase:
   # print(frase[cont], cont)
    letra = frase[cont]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    cont += 1
print(nova_string)