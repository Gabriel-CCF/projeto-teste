def idade_pessoa():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        return True
    else:
        return False


if idade_pessoa() == True:
    print("Pode entrar na Festa")
else:
    print("entrada proibida")
