secreta = 'computador'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Você pode digitar APENAS UMA letra! ')
        continue

    digitadas.append(letra)


    if letra in secreta:
        print(f'A palavra secreta contem a letra {letra} digitada!')
    else:
        print('Aff! Tente novamente!')
        digitadas.pop()

    secreta_temporaria = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temporaria += letra_secreta
        else:
            secreta_temporaria += '*'

    if secreta_temporaria == secreta:
        print(f'VOCÊ GANHOU! A PALAVRA SECRETA ERA {secreta_temporaria}.')
        break
    else:
        print(f'A palavra secreta está assim {secreta_temporaria}!')

    if letra not in secreta:
        chances -= 1

    print()