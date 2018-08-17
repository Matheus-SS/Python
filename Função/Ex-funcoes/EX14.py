# Escreva uma função que calcule o fatorial de um número
# (um inteiro não negativo). Envie o valor
# do número que será calcula como argumento da função.

# valor=0
# x = 10
# y = x-1       TESTANDO FATORIAL /OS DOIS FUNCIONAMO
# for i in range(y,0,-1):
#     x*=i
#
# print(x)

def func(x):
    if(x==0):
      return 1
    else:
        y=x-1
        for i in range(y,0,-1):
          x = (x*i)
        return x

print(func(0))

# def fat(x):
#     if (x == 0 or x == 1):
#         return 1
#
#     else:
#         return x * fat(x - 1)
#
#
# print(fat(6))

