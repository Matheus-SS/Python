# Escreva um função que some todos os
# números contidos numa lista.

lista = [1,2,3,4,5]

def func(*lista):
    num = 0
    for i in range(len(lista)):
        num+=lista[i]
        i+=1
    print(num)

func(*lista)
