# Escreva uma função que multiplique
# todos os números de uma lista.

lista = [1,2,3,4,5]
 #aqui e multiplicado por 1 e nao por zero porque na
# multiplicaçao o 1 é um numero neutro ou seja qualquer numero que
# eu multiplicar por ele sera o proprio numero
def func(*lista):
    num = 1
    for i in range(len(lista)):
        num*=lista[i]
        i+=1
    print(num)

func(5,4,3)