#import random Nos va a importar toda la libreria. 
from random import choice 
from time import sleep 
from os import system
#Listas de las categorías que debemos adivinar en el juego

categorias = ["Nombre", "Fruta", "Lugar", "Animal"]
puntosTotales = 0
contadorRodas = 0
"""
1. Elegir la letra para jugar
2. Mostrar categorías
3. Preguntar los valores de las categorías
4. Preguntar puntos
5. Sumar puntos a Totales
6. Preguntar si quieres seguir jugando
"""
while True: 
#Elegir una letra random del abecedario

    letra = choice("abcdefghijklmnopqrstuvwxyz")
    print(f"\n¡Comienza la ronda {contadorRodas}, con la letra: {letra.upper()}!")
    print("Categoría: ", ", ".join(categorias))

    print("Pensando...")
    sleep(3)
    print("Categorías disponibles:", ", ".join(categorias))
    categoria_inicio = input("¿Por qué categoría quieres iniciar? ")

    palabras = {}#Diccionario para almacenar las palabras que ingrese el usuario por categoría
    for categoria in categorias:
        palabra = input(f"\nCon la letra {letra.upper()}, introduce {categoria}: ")
        palabras[categoria] = palabra

        print("\nTus entradas fuergo: ")
        for categoria, palabra in palabras.items():
            print(f"{categoria} ---> {palabra.capitalize()}")

        sleep(3)


    print("\n--Ingresa tus puntos por categoría--")
    puntosRonda = 0
    for categoria in categorias:
        puntosCategoria = input (f"Puntos obtenidos en {categoria}: ")
        if puntosCategoria == "" or puntosCategoria.isalpha():
            puntosCategoria = 0
        else:
            puntosRonda += int(puntosCategoria)
            print(f"\nPuntos Ronda: {puntosRonda}")
            puntosTotales += puntosRonda

    sleep(5)
    system("clear")

    continuar = input("\n¿Quieres seguir jugando? (s/n)")
    if continuar.lower() !="s":
        break


print("\nPuntos Totales: ", puntosTotales)
print("¡Adiós")