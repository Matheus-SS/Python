senha=1234
senha1 = int(input("Digite a senha:"))
if(senha1==senha):
    print("Acesso permitido")
else:
    for i in range(3):
      print("Você digitou a senha errada.")
      senha1 = int(input("digite a senha:"))
      if(senha1==senha):
         print("Acesso Permitido")
         break
    else:
        print("Acesso Bloqueado.Errou 3 tentativas.")
        exit()

nome = input("Digite seu nome por favor:")
meudia = input("Olá,como foi seu dia hoje "+str(nome)+"?")