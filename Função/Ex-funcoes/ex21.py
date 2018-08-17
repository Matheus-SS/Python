# Escreva uma função que tenha definida uma função em seu escopo.Invoque a função
# aninhada, retorne algum
# valor, imprima esse valor na tela e finalize a aplicação.

def func():
    print("meu nome é matheus")

    def func_interna():
        print("tenho 20 anos")

    func_interna()

func()