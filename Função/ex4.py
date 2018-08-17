#Argumentos posicionais e argumentos nomeados

def dados_pessoais(nome,sobrenome,idade,sexo):
    if (sexo is True):
        sexo = "M"
    else:
        sexo="F"
    print("Nome:{}\nSobrenome:{}\nIdade:{}\nSexo:{}"
          .format(nome,sobrenome,idade,sexo))


#dados_pessoais("Claudio","Silva",30,True)
dados_pessoais(idade =30,
                sexo=True,
                nome="Claudio",
               sobrenome="Carvalho"

               )