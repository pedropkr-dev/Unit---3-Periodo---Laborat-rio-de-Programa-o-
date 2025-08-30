def numPrimos(num):
    if num <= 1:
        print('Número não primo')
        return
    for c in range(2, num):
        if num % c == 0:
            print ('Número não primo')
            return
    print('Número primo')
input = int(input("Digite um número: "))

numPrimos(input)