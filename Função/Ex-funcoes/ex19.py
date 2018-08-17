# Escreva uma função que imprima somente os números pares
# Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Saída: [2, 4, 6, 8]
lista=[1,2,3,4,5,6,7,8,9]

def func(*args):
    for i,j in enumerate(args):
        if j%2==0:
            print(j,end="/")



func(1,2,4,5,6,7,8,912,43,54)