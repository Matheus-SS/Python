# Escreva uma função que aceite Strings e calcule a
# quantidade de letras em mauisculas e minúsculas que a String possui.


def func(x):
    mi=0 #DEFINIR AS DUAS VARIAVEIS Q SERAO INCREMENTADAS
    ma=0
    for k, v in enumerate(x):# ESSE FOR ENUMERATE FAZ RODAR TODAS AS POSICOES DA STRING ATE O SEU FINAL DANDO O
                                #  INDICE E O VALOR DA STRING , O K ME DA O INDICE E O V O VALOR NO NOSSO CASO A LETRA

        if (v.islower()):   #AKI NESSES DOIS IF's EU COMPARO SE A LETRA Q ESTA RODANDO E
                            # MINUSCULA OU MAIUSCULA COM AS FUNÇOES ISLOWER E ISUPPER E VOU INCREMENTANDO AS
                            # VARIAVEIS NO FINAL É SO EXIBIR
            mi+=1
        if(v.isupper()):
            ma+=1

    print("minuscula: {} / MAIUSCULA: {}".format(mi,ma))


func("Hello World")



# for i in range(len(lista.lower())):
#        num += lista[i]
#        i += 1
