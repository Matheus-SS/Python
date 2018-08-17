# Escreva uma função que receba como argumento uma lista
# que poderá ter valores duplicados e retorne uma
# nova lista sem que haja valores iguais.


def func(*args):
    x=set(args)
    print(x)
func(1,1,1,1,1,1,1,1,1,1,1)

