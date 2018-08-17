login="abcd"
senha=1234
login1 = input("Digite o login:")
senha1 = int(input("Digite a senha:"))

while(senha1!=senha) or (login1!=login):
    print("Login ou senha errada , digite novamente.")
    login1 = input("Digite o login:")
    senha1 = int(input("Digite a senha:"))
else:
    print("Acesso permitido")
print("")
nome = input("Digite seu nome por favor:")
meudia = input("Olá,como foi seu dia hoje "+str(nome)+"?")