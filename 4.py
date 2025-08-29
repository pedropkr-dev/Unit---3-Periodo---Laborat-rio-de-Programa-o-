def impar_ou_par(impar): 
    if impar %2 != 0:
        return
        print("Seu número é impar")
    else:
        print("Seu número é par")
    
number = int(input("Insira um número e verifique se ele é impar ou par: "))

impar_ou_par(number)