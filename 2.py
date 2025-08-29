def anoBissexto(ano):
    if ano % 4 == 0 and ano % 400 == 0:
        print("Sim. Seu ano é bissexto.") 
    else:
        print("Não. Seu ano não é bissexto.")

ano = int(input("Insira um ano: "))

anoBissexto(ano)