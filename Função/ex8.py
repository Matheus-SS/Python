#DESEMPACOTAMENTO
def pessoa(nome,sobrenome,idade):
    print(nome)
    print(sobrenome)
    print(idade)

#lista = ["Excript","Brasil",20]

# pessoa(tupla[0],tupla[1],tupla[2])
#pessoa(*lista)


d={"nome":"Excript","sobrenome":"Brasil","idade": 20}
pessoa(**d)