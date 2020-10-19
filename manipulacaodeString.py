'''
manipulaçao de strings - aula 6
*STRINGS INDICES
*FATIAMENTO DE STRINGS [INICIO:FIM:PASSO]
*FUNÇOES BUILT-IN LEN, ABS, TYPE, PRINT, ETC...

ESSAS FUNÇOES PODEM SER USADAS DIRETAMENTE EM CADA TIPO.
VOCE PODE CONFERIR TUDO ISSO EM:
HTTPS://DOCS.PYTHON.ORG/3/LIBRARY/STDTYPES.HTML (TIPOS BUILT-IN)
HTTPS://DOCS.PYTHON.ORG/3/LIBRARY/FUNCTIONS.HTML (FUNÇOES BUILT-IN)
'''


# indices positivos no texto de 0a7
texto = 'Python_s28'
print(texto[5])#acessando o caracters pelo indice

# indices negativos no texto de -9 a -1 -[987654321]
url = 'www.goole.com.br/'
print(url[:-2])

nova_string = texto[:6]
print(nova_string)

nova_string = texto[7:]
print(nova_string)

nova_string = texto[-1:]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[0:6:2]
print(nova_string)
nova_string = texto[0::3]
print(nova_string)

print(len(texto))