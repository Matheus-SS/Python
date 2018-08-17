# Escreva uma função que verifique se um número está num intervalo determinado.



def func(x,y,z):    #A FUNCAO TERA TRES PARAMENTROS X E Y SAO OS PARAMETROS DE INTERVALO E Z É O VALOR A SER VERIFICADO
    lista = [x,y]   #AKI É UMA LISTA QUE RECEBE OS DOIS PARAMETROS
    k = min(lista)  #DIZER QUAL O MENOR VALOR DA LISTA
    l = max(lista)  #DIZER QUAL O MAIOR VALOR DA LISTA
    if(k<=z<=l):    #AKI ESTA ORGANIZADO COM O INTERVALO DE MENOR VALOR / O VALOR DIGITADO / O INTERVALO DE MAIOR VALOR
        print("PERTENCE AO INTERVALO")
    else:
        print("NÃO PERTENCE AO INTERVALO")

func(54,90,)# OS DOIS PRIMEIROS VALORES SAO OS INTERVALOS
# E O ULTIMO É O VALOR Q VC QUER VERIFICAR ,NAO IMPORTA A ORDEM
# DOS DOIS PRIMEIROS ,APENAS O TERCEIRO DE SER O VALOR A SER VERIFICADO

# print(max(lista))
# x=max(lista)
# print(min(lista))
# y =min(lista)