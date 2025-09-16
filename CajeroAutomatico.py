#Crea un programa que simule un cajero con un saldo inicial.
#- Menú con opciones: consultar saldo, retirar, depositar o salir.
#- Si se retira, verificar que el saldo sea suficiente.
#- Si se deposita, sumar el monto al saldo.
#- Mostrar mensajes claros en cada operación.

print("---- Bienvenida a BBVA ---")
print("-°-°-°-°-Menú de Opciones-°-°-°-°-")
print("1. Consultar saldo")
print("2. Retirar")
print("3. Depositar")
print("4. salir")

opcion = input("Escoja la opción deseada (1-4): ")
saldoinicial = 1500
if opcion == "1":
    print(f"Su saldo es: {saldoinicial}")
elif opcion == "2":
    aretiro = float (input("Cuantos deseas retirar: ")) 
    if aretiro <= saldoinicial:
        saldoinicial = saldoinicial-aretiro
        print(f"Su saldo es: {saldoinicial}")
    else:
        print("Su saldo es insuficiente")
elif opcion == "3":
    bdeposito = float (input("Cuantos deseas depostiar: ")) 
    saldofinal = saldoinicial + bdeposito
    print(f"Su saldo es: {saldofinal}")
elif opcion == "4": 
  print("Gracias, Vuelva pronto")
else:
    print("Gracias, Vuelva pronto")
