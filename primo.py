import os

os.system("cls")

print("\t\t\tIdentificador de Numeros Primos")
numero = int(input("Ingrese un número para saber si es primo o no: "))

if numero <= 1:
    print("El número no es primo")
else:
    limite = int(numero**0.5)
    es_primo = True
    divisor = 2

    while divisor <= limite:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1

    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")

input("\nPresiona Enter para salir")
