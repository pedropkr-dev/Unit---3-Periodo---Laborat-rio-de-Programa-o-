def impar_ou_par(impar): 
    if impar %2 != 0:
        print("O número é impar")
    else:
        print("O número não é impar")
    
number = int(input("Insira um número e verifique se ele é impar: "))

impar_ou_par(number)