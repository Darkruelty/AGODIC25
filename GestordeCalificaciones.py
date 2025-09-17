#Ejercicio 4. Gestor de Calificaciones
#Crea un programa que gestione calificaciones de tres parciales.
#Opciones: calcular promedio, calcular calificación final con ponderaciones, mostrar mayor y menor calificación, 
# verificar si el alumno aprueba o reprueba.
#El programa debe pedir las calificaciones solo cuando se necesiten.
#El usuario deberá proveer las tres calificaciones de los parciales y además pide las ponderaciones 
# p.ej. 30% + 30% + 40%, de modo que puedas calcular tus calificaciones según la materia y sus ponderaciones.


print("---- Gestor de Calificaciones ---")
print("---- Ponderacion del parcial ---")
aponderacion = float (input("Ingresa la ponderacion de las practicas del parcial: "))
bponderacion = float (input("Ingresa la ponderacion del examen parcial: "))
cponderacion = float (input("Ingresa la ponderacion del proyecto del parcial: "))
print("---- Calificaciones del primer parcial ---")
acalificacion = float (input("Ingresa la calificación de las practicas del primer parcial: "))
bcalificacion = float (input("Ingresa la calificación del examen del primer parcial parcial: "))
ccalificacion = float (input("Ingresa la calificación del proyecto del primer parcial: "))
print("---- Calificaciones del segudno parcial ---")
dcalificacion = float (input("Ingresa la calificación de las practicas del segundo parcial: "))
ecalificacion = float (input("Ingresa la calificación del examen del primer segundo parcial: "))
fcalificacion = float (input("Ingresa la calificación del proyecto del segudo parcial: "))
print("---- Calificaciones del tercer parcial ---")
gcalificacion = float (input("Ingresa la calificación de las practicas del tercer parcial: "))
hcalificacion = float (input("Ingresa la calificación del examen del primer tercer parcial: "))
icalificacion = float (input("Ingresa la calificación del proyecto del tercer parcial: "))


acalificacionfinal = (((aponderacion*acalificacion)+(bponderacion*bcalificacion)+(cponderacion*ccalificacion))/100)
bcalificacionfinal = (((aponderacion*dcalificacion)+(bponderacion*ecalificacion)+(cponderacion*fcalificacion))/100)
ccalificacionfinal = (((aponderacion*gcalificacion)+(bponderacion*hcalificacion)+(cponderacion*icalificacion))/100)


promediofinal = ((acalificacionfinal + bcalificacionfinal + bcalificacionfinal)/3 )

print("---- Calificaciones de los parciales ---")
print(f"La calificación del primer parcial: {acalificacionfinal}")
print(f"La calificación del segundo parcial: {bcalificacionfinal}")  
print(f"La calificación del tercer parcial: {ccalificacionfinal}") 

print("---- Calificaciones mayor y menor ---")
mayor = acalificacionfinal
menor = acalificacionfinal
if bcalificacionfinal > mayor:
    mayor = bcalificacionfinal
elif bcalificacionfinal < menor:
    menor = bcalificacionfinal

if ccalificacionfinal > mayor:
    mayor = ccalificacionfinal
elif ccalificacionfinal < menor:
    menor = ccalificacionfinal

print(f"La calificación mayor es: {mayor}")
print(f"La calificación menor es: {menor}") 

print(f"La calificación final de la materia: {promediofinal}") 

if ccalificacionfinal >= 70:
    print(f"La calificación de la materia es aprobatoria") 
elif ccalificacionfinal < 70:
    print(f"La calificación de la materia es reprobatoria") 



   