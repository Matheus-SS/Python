# Escreva uma função que inverta a ordem dos
# elementos de uma lista manualmente.
# Não utilize a função interna do Python que faz
# inverção, crie o algoritmo que faça a inversão.


# print(len(lista))
# print(x)
# print(lista[-1])  TESTE DA LISTA
# print((lista[-1]))
# print(lista[x])

lista= "1234abcd"
def func (*lista):
    x= len(lista)-1
    for i in range(x,-1,-1):
        print(lista[i])


# def lista(x):
#     print(x[::-1])        TAMBEM FUNCIONA
#
# lista("1234abcd")

func(*lista)