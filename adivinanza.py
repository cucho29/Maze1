import os
import random

os.system("cls")
print("\t\t\tAdivinanza del Numero Secreto")
numero_secreto = random.randint(1, 25)

intentos = 0

while True:
    intentos += 1
    
    numero_usuario = int(input("Ingresa un número entre 1 y 25: "))
    
    if numero_usuario == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif numero_usuario > numero_secreto:
        print("El número es demasiado alto. Intenta nuevamente.")
    else:
        print("El número es demasiado bajo. Intenta nuevamente.")

print(f"\nGracias por jugar. El número secreto era: {numero_secreto}")

input("\nPresiona Enter para salir")