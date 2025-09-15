print("---- Calculador de Palabras----")
print("Menú de opciones: ")
print("1. Contar caracteres")
print("2. Pasar a MAYÚSCULAS")
print("3. Pasar a minúsculas")
print("4. contar cuantas veces aparece una letra")
print("5. Reemplazar una letra por otra")
print("6. Unir cada letra con guiones")
print("7. Sumar la longitud de String")
print("Salir")

texto= input("Ingresa una palabra o sentencia: ")
opcion = input("Elige una opción del menú (1-8): ")
conteodecartacteres = len(texto)
if opcion == '1':
   conteodecartacteres = len(texto)
   print("Número de caracteres: "+str(len(texto)))
   print("Número de caracteres: ", conteodecartacteres)
   print(f"Número de caracteres:  {conteodecartacteres}")
   print(f"Número de caracteres: {len(texto)}")

elif opcion == '2':
    texto_en_mayusculas = texto.upper()
    print("Número de caracteres: ", texto_en_mayusculas)
elif opcion == '3':
   texto_en_minusculas = texto.lower()
   print("Número de caracteres: ", texto_en_minusculas)
elif opcion == '4':
   letra_a_contar=input("Ingresa la letra a contar: ")
   conteo_de_letra = texto.count(letra_a_contar)
   print(f"La letra' {letra_a_contar}' aparece {conteo_de_letra} veces en la cadena.")

elif opcion == '5':
    letra_a_reemplazar= input("Ingresa la letra a reemplzar ")
    nuevo_caracter= input("Ingrese el nuevo caracter ")
    texto_modificado = texto.replace(letra_a_reemplazar, nuevo_caracter)
    print("Este es el texto modificado:", texto_modificado)
elif opcion == '6':
    parte2 = input("Ingresa el texto 2: ")
    parte3 = input("Ingresa el texto 3: ")
    parte4 = input("Ingresa el texto 4: ")
    partes = [texto, parte2, parte3, parte4]
    resultado = '-'.join(partes)
    print (resultado)
elif opcion == '7':
    sentencia2 = input("Ingresa el texto 2: ")
    mi_string = texto + " "+ sentencia2
    longitud = len(mi_string)
    print(f"La longitud de '{mi_string}' es: {longitud}")
elif opcion == '8':
    print("Procesando...")
    print("Adiós")
else:
    print("Opción incorrecta, debes ")
