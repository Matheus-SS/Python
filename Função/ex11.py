#INSTRUÇÃO NONLOCAL

def func():

    var_local =10
    def func_interna():
        nonlocal var_local
        var_local+=1
        print(var_local)

    func_interna()

func()
x= 10
def funcx():
    global x
    return x
print(funcx())