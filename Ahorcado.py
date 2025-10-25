"""También escribe el código para un juego del ahorcado, 
donde podrás utilizar una lista para almacenar las palabras que 
serán utilizadas en el juego, y la función choice de la librería 
random para elegir una palabra distinta cada vez que el juego se ejecute. 
Además, se deberá presentar en pantalla una serie como esta: _ _ _ _ _ _ _ _ _ 
donde le dará al usuario la idea de cuántas letras forman la palabra secreta. 
El usuario podrá ingresar letra por letra y el sistema mostrará si es 
el caso la letra encontrada, si no lo es,  restará una vida, en este juego el usuario cuenta con 3 vidas. """
from random import choice 
from time import sleep 
from os import system


palabra=["metoclopramida", "paracetamol", "ibuprofeno"]
tupalabra=""
vidas=5
palabra_aleatoria = choice(palabra)

while vidas > 0:
    print("Empecemos, comienza a adivinar")
    fallas=0
   
    for letra in palabra_aleatoria:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print("_", end="")
            fallas+=1
        
    if fallas == 0:
        print(" ")
        print("felicitaciones ganaste")
    
        continuar = input("\n¿Quieres seguir jugando? (s/n)")
        if continuar.lower() !="s":
            break
        else:
            # Reiniciar juego
            print("Empecemos, comienza a adivinar")
            palabra_aleatoria = choice(palabra)
            tupalabra = ""
            vidas = 5    

    tuletra=input("\nIntroduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra_aleatoria:
        vidas -= 1
        print("La letra no esta en la palabra")
        print("Tenes ", +vidas, "vidas")
    if vidas == 0:
        print("PERDISTE!")

        continuar = input("\n¿Quieres seguir jugando? (s/n)")
        if continuar.lower() !="s":
            break
        else:
            # Reiniciar juego
            palabra_aleatoria = choice(palabra)
            tupalabra = ""
            vidas = 5      

