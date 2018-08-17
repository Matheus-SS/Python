# Escreva um algoritmo capaz de receber uma quantidade
# variável de parâmetros que estejam associados a
# uma chave. Em seguida, imprima na tela o nome da chave
# e o respectivo valor:
#TRANSFORMAR DUAS LISTAS EM DICIONARIOS
d1=[]
d2=[]
x=1
y=1
z=1
while True:
    x = input("Digite a CHAVE:")
    d1.append(x)
    y = input("Digite o VALOR:")
    d2.append(y)
    z=input("Digite zero para sair ou qualquer outra tecla para continuar:")
    if(z=="0"):
        break
    else:
        continue
print(dict(zip(d1,d2)))
print(d2[0])




