#from math import * #Nos importamos toda la librería
#from math import sqrt, pi #aquí importamos la función de raíz cuadrada y el valor de pi
from math import pi #importamos solo el valor de la constate pi

print("---- Bienvenida a mi Calculadora de Figuras ---")
print("-°-°-°-°-Menú de figuras-°-°-°-°-")
print("1. Cubo")
print("2. Prisma")
print("3. Pirámide")
print("4. Cilindro")
print("5. Cono")
print("6. Esfera")
figura = input("Figura (1-6): ")
print("-°-°-°-°-Menú de opciones-°-°-°-°-")
print("1. Calcular el área")
print("2. Calcular el volumen")
print("3. Calcular ambos")
print("4. Salir")
opcion= input("Figura (1-4): ")
if opcion == "1": #Este if controla que quiere el usario calcular.
    if figura == "1": # este if anidado controlan la figura para calcular el área.
        lado = float (input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2}")
    elif figura == "2":
        aladobase = float (input("lado base A (cm):"))
        bladobase = float (input("lado base B (cm):"))
        altura = float (input("Altura (cm):"))
        rectangulo1 = (aladobase * bladobase)
        rectangulo2 = (bladobase * altura)
        rectangulo3 = (altura * aladobase)
        areaprisma = ((rectangulo1 * 2) + (rectangulo2 * 2) + (rectangulo3 * 2))
        print(f"El área del prisma es: {areaprisma}")
    elif figura == "3":
        aladobase = float (input("lado base de la pirámide (cm):"))
        baltura = float (input("Altura de la pirámide (cm):"))
        apotema = float (input("Apotema de la Pirámide (cm):"))
        areacaralateral= (((aladobase * apotema)/2)*4)
        areadelabase = (aladobase * aladobase)
        areaPiramide = (areacaralateral + areadelabase)
        print(f"El Área de la pirámide es:  {areaPiramide}")
    elif figura == "4":
        aradio = float (input("Radio del cilindro (cm):"))
        baltura = float (input("Altura del Cilindro (cm):"))
        areadelcilindro = ((2*pi*aradio**2) + (2*pi*aradio*baltura))
        print(f"El Área del cilindro:  {areadelcilindro}")
    elif figura == "5":
        bradio = float (input("Radio del cono (cm):"))
        generatriz = float (input("Generatriz del cono (cm):"))
        arealateral= (pi*(bradio*generatriz))
        areadelabase = (pi*bradio**2)
        areaPiramide = (arealateral + areadelabase)
        print(f"El Área del cono es:  {areaPiramide}")
    elif figura == "6":
        bradio = float (input("Radio de la esfera (cm):"))
        areaesfera= (4 * pi*bradio**2)
        print(f"El Área de la esfera es:  {areaesfera}")
    else:
        print("No conozco esa figura. ")
elif opcion == "2":# este if anidado controlan la figura para calcular el volumen.

    if figura == "1": 
        lado = float (input("Lado (cm):"))
        VolumenCubo = lado**2
        print(f"El volumen del cubo es: {VolumenCubo:.2}")
    elif figura == "2":
        aladobase = float (input("lado base A (cm):"))
        bladobase = float (input("lado base B (cm):"))
        altura = float (input("Altura (cm):"))
        areadelabase = (aladobase * bladobase)
        volumenPrisma = (areadelabase*altura)
        print(f"El Volumen del prisma es: {volumenPrisma}")
    elif figura == "3":
        aladobase = float (input("lado base de la pirámide (cm):"))
        baltura = float (input("Altura de la pirámide (cm):"))
        apotema = float (input("Apotema de la Pirámide (cm):"))
        areadelabase = (aladobase * aladobase)
        volumenPiramide = ((areadelabase*baltura)/3)
        print(f"El Volumen de la pirámide es: {volumenPiramide}")
    elif figura == "4":
        aradio = float (input("Radio del cilindro (cm):"))
        baltura = float (input("Altura del Cilindro (cm):"))
        Vdelcilindro = (pi*(aradio**2)*baltura)
        print(f"El Volumen del cilindro:  {Vdelcilindro}")
    elif figura == "5":
        bradio = float (input("Radio del Cono (cm):"))
        baltura = float (input("Altura del Cono (cm):"))
        generatriz = float (input("Generatriz del Cono (cm):"))
        areadelabase = (pi*bradio**2)
        areaPiramide = ((areadelabase*baltura)/3)
        print(f"El Volumen del cono es:  {areaPiramide}")
    elif figura == "6":
        bradio = float (input("Radio de la esfera (cm):"))
        Volumenesfera= ((4/3) * pi*bradio**3)
        print(f"El Volumen de la esfera es:  {Volumenesfera}")
    else:
        print("No conozco esa figura. ")

elif opcion == "3":# este if anidado controlan la figura para calcular el área y volumen.

    if figura == "1": 
        lado = float (input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2}")
        VolumenCubo = lado**2
        print(f"El volumen del cubo es: {VolumenCubo:.2}")
    elif figura == "2":
        aladobase = float (input("lado base A (cm):"))
        bladobase = float (input("lado base B (cm):"))
        altura = float (input("Altura (cm):"))
        rectangulo1 = (aladobase * bladobase)
        rectangulo2 = (bladobase * altura)
        rectangulo3 = (altura * aladobase)
        areaprisma = ((rectangulo1 * 2) + (rectangulo2 * 2) + (rectangulo3 * 2))
        print(f"El área del prisma es: {areaprisma}")
        areadelabase = (aladobase * bladobase)
        volumenPrisma = (areadelabase*altura)
        print(f"El Volumen del prisma es: {volumenPrisma}")
    elif figura == "3":
        aladobase = float (input("lado base de la pirámide (cm):"))
        baltura = float (input("Altura de la pirámide (cm):"))
        apotema = float (input("Apotema de la Pirámide (cm):"))
        areacaralateral= (((aladobase * apotema)/2)*4)
        areadelabase = (aladobase * aladobase)
        areaPiramide = (areacaralateral + areadelabase)
        print(f"El Área de la pirámide es: {areaPiramide}")
        areadelabase = (aladobase * aladobase)
        volumenPiramide = ((areadelabase*baltura)/3)
        print(f"El Volumen de la pirámide es: {volumenPiramide}")
    elif figura == "4":
        aradio = float (input("Radio del cilindro (cm):"))
        baltura = float (input("Altura del Cilindro (cm):"))
        areadelcilindro = ((2*pi*aradio**2) + (2*pi*aradio*baltura))
        print(f"El Área del cilindro:  {areadelcilindro}")
        Vdelcilindro = (pi*(aradio**2)*baltura)
        print(f"El Volumen del cilindro:  {Vdelcilindro}")
    elif figura == "5":
        baltura = float (input("Altura del Cono (cm):"))
        bradio = float (input("Radio del Cono (cm):"))
        generatriz = float (input("Generatriz del Cono (cm):"))
        arealateral= (pi*(bradio*generatriz))
        areadelabase = (pi*bradio**2)
        areaPiramide = (arealateral + areadelabase)
        print(f"El Área del cono es:  {areaPiramide}")
        areadelabase = (pi*bradio**2)
        areaPiramide = ((areadelabase*baltura)/3)
        print(f"El Volumen del cono es:  {areaPiramide}")
    elif figura == "6":
        bradio = float (input("Radio de la esfera (cm):"))
        areaesfera= (4 * pi*bradio**2)
        print(f"El Área del cono es:  {areaesfera}")
        Volumenesfera= ((4/3) * pi*bradio**3)
        print(f"El Volumen de la esfera es:  {Volumenesfera}")
    else:
        print("Opción incorrecta, adiós. =D")



