# Escreva uma função que verifica se uma String enviada é um palíndromo ou não.


def func(valor):
    x=(valor[::-1])
    if valor == x:
        print("palindromo")
    else:
        print("Nao palindromo")

func("arara")