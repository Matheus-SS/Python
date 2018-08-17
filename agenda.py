
lista = []
print("1 - Adicionar contato")
print("2 - Remover contato")
print("3 - Atualizar contato")
print("4 - Listar contato")
print("0 - Sair")
print()

while True:
    n_digitado = int(input("O que deseja fazer:"))
    print()
    if(n_digitado==0):
        break
    if(n_digitado==1):
        res=input("Deseja voltar o menu digite Y senao aperte qualquer "
                  "outra tecla para continuar:")
        if (res == 'Y' or res == 'y'):
            continue
        nome = input("Digite nome:")
        num = int(input("Digite numero de Telefone:"))
        print()
        lista.append([nome,num])
    if(n_digitado == 2):
        print(list(enumerate(lista)))
        print()
        res = input("Deseja voltar o menu digite Y senao aperte qualquer "
                    "outra tecla para continuar:")
        if (res == 'Y' or res == 'y'):
            continue
        x = int(input("Digite o numero que vem antes do nome "
                      "para que seja excluido o contato:"))
        lista.pop(x)
    if(n_digitado==3):
        res = input("Deseja voltar o menu digite Y senao aperte qualquer "
                    "outra tecla para continuar:")
        if (res == 'Y' or res == 'y'):
            continue
        y = int(input("Qual contato dejesa alterar - digite o seu indice : "))
        x = int(input("Se deseja alterar o NOME digite 1,alterar NUMERO digite 2: "))
        if(x==1):
            z=input("Digite o nome:")
            lista[y][0] = z
        if (x == 2):
            z = int(input("Digite o Numero:"))
            lista[y][1] = z
    if(n_digitado==4):
        res = input("Deseja voltar o menu digite Y senao aperte qualquer "
                    "outra tecla para continuar:")
        if (res == 'Y' or res == 'y'):
            continue
        print()
        print(list(enumerate(lista)))


