print("---- Conversor de Unidades ---")
print("-°-°-°-°-Menú de Opciones-°-°-°-°-")
print("1. Temperatura: Celsius → Fahrenheit")
print("2. Temperatura: Fahrenheit → Celsius")
print("3. Longitud: Metros → Centímetros")
print("4. Longitud: Centímetros → Metros")
print("5. Masa: Kilogramos → Gramos")
print("6. Masa: Gramos → Kilogramos")

opcion = input("Escoja la opción deseada (1-6): ")

if opcion == "1":
    celsius = float (input ("Ingresa la Temperatura en grados celsius: "))
    cfahrenheit = ((celsius * (9/5))+32)
    print(f"La conversion a Fahrenheit es: {cfahrenheit}")
elif opcion == "2":
    fahrenheit = float (input ("Ingresa la Temperatura en grados Fahrenheit: "))
    ccelsius = ((fahrenheit-32)*(5/9))
    print(f"La conversion a Fahrenheit es: {ccelsius}")
elif opcion == "3":
    metros = float (input ("Ingresa la longitud en metros: "))
    ccentrimetros = (metros * 100)
    print(f"La conversion a centimetros es: {ccentrimetros}")
elif opcion == "4": 
    centimetros = float (input ("Ingresa la longitud en centimetros: "))
    cmetros = (centimetros / 100)
    print(f"La conversion a centimetros es: {cmetros}")
elif opcion == "5": 
    kilogramos = float (input ("Ingresa la masa en Kilogramos: "))
    cgramos = (kilogramos * 1000)
    print(f"La conversion a Gramos es: {cgramos}")
elif opcion == "6": 
    gramos = float (input ("Ingresa la masa en Gramos: "))
    ckilogramos = (gramos / 1000)
    print(f"La conversion a Gramos es: {ckilogramos}")
else:
    print("Gracias, Vuelva pronto")