# Escreva uma função capaz de receber uma quantidade indeterminada de
# parâmetros e imprima na telas os números primos contidos nessa lista.



def func(*args):
    x = (sorted(set(args)))     #faz com q os numeros fiquem em ordem crescente e sem repeticao
    tot = 0
    for i,j in enumerate(x):    #me da o valor e a posicao dos numeros na lista o j me da o valor e o i o indice
        # print(i,j)
        for c in range (1, j+1):    #faz o valor mais um pois o range sempre faz menos um o valor ,ex:se o valor e 10 o range vai ate 9
            if j % c ==0:
                print('\033[33m',end='')
                tot+=1                      #incrementa a variavel cada vez que acha um numero q é divisivel
            else:
                print('\033[31m',end='')
            print('{}'.format(c),end='')
        print('\n\033[mO numero {} foi divisivel {} vezes'.format(j,tot))
        if tot ==2: #condicao q verifica se o numero foi dividido duas vezes ele e primo
            print("PRIMO")
        else:
            print("NAO PRIMO")
        tot =0

func(2,10,13,15)


