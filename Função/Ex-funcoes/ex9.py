# Escreva um algoritmo capaz de receber uma
# quantidade variável de parâmetros que estejam
# associados a uma chave. Em seguida, imprima
# na tela o nome da chave e o respectivo valor:

def func(a, b, c, d):
    print(a+b+c+d)
lista = 1,2,3,4

func(*lista)