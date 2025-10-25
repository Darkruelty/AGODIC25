def saludar ():
    prinf("¡Hola desde la función saludar")

if "_name_"=="_main_":
    prinf(" Este mensaje solo aparece al ejecutar DIRECTAMENTE")
    saludar()

for i in range(5):
    print(i)
i=i+1


edad = 25

resultado =(5*6) + 2 - (4/2)
print(resultado)
import pdb
pdb.set_trace()

divisor = input("Divisor = ")
dividendo = input("Dividendo = ")

try:
    division = int(divisor)/int(dividendo)
    print("Resultado:", division)
except ZeroDivisionError as error:
    print("No se puede dividir por 0.")
except ValueError as error:
    print("Solo se pueden dividir datos numéricos")
except:
    print("An unexpected error occurred!")


print("Aquí continuamos...")