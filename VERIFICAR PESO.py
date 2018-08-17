cont =[]
lista = []
maior= menor =0
while True:

    nome = input("digite seu nome:")
    peso = int(input("digite seu peso:"))
    res = input("Deseja continuar? ").lstrip().upper()[0]
    lista.append(nome)
    lista.append(peso)
    if len(cont)==0:
        maior = menor = lista[1]
    else:
        if lista[1]>maior:
            maior=lista[1]
        if lista[1]<menor:
            menor = lista[1]
    cont.append(lista[:])#faz com que eu adicione essas duas listaem outra lista

    lista.clear()
    if(res=="S"):
       continue
    else:
        break

print(f'O dados foram {cont}')
print(f'Ao todp vc cadastrou {len(cont)}')
print(f'Menor {menor}')
print(f'Maior {maior}')