#FUNÇÃO VARIADICA

def lista_de_argumentos(*args): #lista
    print(args)

def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)

def argumentos(*args,**kwargs):
    print(args)
    print(kwargs)

argumentos(1,2,3,4)

# lista_de_argumentos(1,2,3,4,5,6)
# lista_de_argumentos("um","dois","tres","quatro")
#
# lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)
# lista_de_argumentos_associativos(um=1,dois=2,tres=3,quatro=4)