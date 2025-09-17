#Ejercicio 5. Tienda / Cotizador Simple
#Crea un programa que simule compras en una tienda.
#Opciones: calcular el total con IVA, calcular total con descuento + IVA, calcular precio unitario dado un total 
# y cantidad, o salir.
#El usuario ingresa precios y cantidades según la opción.
#Investiga cómo se aplica el IVA y cómo calcular descuentos.
#Para (1) y (2), pedir precio y cantidad; calcular subtotal, IVA, total.
#Para (2) aplicar primero descuento, luego IVA. El descuento deberá ingresarse por el usuario como si 
# fuera un cupón con los siguientes valores:
#VERANO = 10%
#SALDOS = 35%
#BBVA = 5%
#BANORTE25 = 25%
#Para (3) pedir total y cantidad; devolver unitario con 2 decimales.



print("---- Bienvenido a su tienda amiga ---")
print("-°-°-°-°-Menú de Opciones-°-°-°-°-")
print("1. Calcular el Total con IVA")
print("2. Calcular el Total con descuento + IVA")
print("3. Calcular precio unitario dando un Total y cantidad")
print("4. salir")
opcion = input("Escoja la opción deseada (1-4): ")

if opcion == '1':
    acantidad = float (input("Ingresa los litros de compra de gasolina : "))
    bprecio = float (input("Ingresa el precio por litro: "))

    subtotal = (acantidad * bprecio)
    iva = (subtotal * 0.16 )
    total = (subtotal + iva )

    print(f"SUBTOTAL: {subtotal}")
    print(f"IVA: {iva}")
    print(f"TOTAL: {total}")

    print("---- Gracias por su compra vuelva prontro ---")
elif opcion == '2':
    acantidad = float (input("Ingresa los litros de compra de gasolina : "))
    bprecio = float (input("Ingresa el precio por litro: "))    
    print("1. Cupón de VERANO = 10%")
    print("2. Cupón de SALDOS = 35%")
    print("3. Cupón de BBVA = 5%")
    print("4. Cupón de BANORTE25 = 25%")
    opcion = input("Escoja la opción deseada (1-4): ")
    if opcion == "1":       
            subtotal = (acantidad * bprecio)
            subtotaldescuento = (subtotal - (subtotal * .10))
            iva = (subtotaldescuento * 0.10 )
            total = (subtotaldescuento + iva )

            print(f"SUBTOTAL CON EL 10% DE DESCUENTO: {subtotaldescuento}")
            print(f"IVA: {iva}")
            print(f"TOTAL: {total}")
            print("---- Gracias por su compra vuelva prontro ---")
    elif opcion == "2":
            subtotal = (acantidad * bprecio)
            subtotaldescuento = (subtotal - (subtotal * .35))
            iva = (subtotaldescuento * 0.35 )
            total = (subtotaldescuento + iva )

            print(f"SUBTOTAL CON EL 35% DE DESCUENTO: {subtotaldescuento}")
            print(f"IVA: {iva}")
            print(f"TOTAL: {total}")
            print("---- Gracias por su compra vuelva prontro ---")
    elif opcion == "3":
            subtotal = (acantidad * bprecio)
            subtotaldescuento = (subtotal - (subtotal * .5))
            iva = (subtotaldescuento * 0.5 )
            total = (subtotaldescuento + iva )

            print(f"SUBTOTAL CON EL 5% DE DESCUENTO: {subtotaldescuento}")
            print(f"IVA: {iva}")
            print(f"TOTAL: {total}")
            print("---- Gracias por su compra vuelva prontro ---")
    elif opcion == "4":
            subtotal = (acantidad * bprecio)
            subtotaldescuento = (subtotal - (subtotal * .25))
            iva = (subtotaldescuento * 0.5 )
            total = (subtotaldescuento + iva )

            print(f"SUBTOTAL CON EL 25% DE DESCUENTO: {subtotaldescuento}")
            print(f"IVA: {iva}")
            print(f"TOTAL: {total}")
            print("---- Gracias por su compra vuelva prontro ---")
    else:
        print("Opción incorrecta, Gracias, Vuelva pronto")
   
elif opcion =='3':
    acantidad = float (input("Ingresa los litros de compra de gasolina : "))
    bprecio = float (input("Ingresa el precio total de la gasolina: "))
    iva = (bprecio * 0.16 )
    subtotalunitario = (bprecio - iva )
    preciounitario = (subtotalunitario / acantidad)
    
    print(f"El precio unitario es: {preciounitario:.2f}")
    print("Gracias, Vuelva pronto")
elif opcion == '4':
    print("Gracias, Vuelva pronto")
else:
    print("Opción incorrecta, Gracias, Vuelva pronto")