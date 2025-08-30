def eh_primo(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  
    return True 


def filtrar_primos(lista):
    primos = []
    for num in lista:
        if eh_primo(num):
            primos.append(num)
    return primos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

lista_de_primos = filtrar_primos(numeros)
print(lista_de_primos)
