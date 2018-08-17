n=0
def func(x,y,z):
    print(x,y,z)
lista = [1,67,2]
lista.sort()
func(*lista)
for i in range(len(lista)):
    n+=lista[i]
print("%.2f" % (n/3))

