frutas = ["kiwi", "fresa", "piña", "uvas", "sandía"]

for fruta in frutas:
    print(f"{frutas.index(fruta)+1}. {fruta}")
print()

milista = ["juli", 12, True, False, 32.124, [1,2,3], "Adíos"]

for item in milista:
    print(f"{milista.index(item)}: {item}")
frutas.append("plátano")
print()

A={1,2,3,4,8}
B={3,4,5,6}
interseccion = set()
print(type(A))
print(type(B))
print(type(interseccion))
print()

for x in A:
    if x in B:
        interseccion.add(x)
print(f"A: {A}, {B}, Intersección: {interseccion}")


tabla_del= input("De qué numero te calculo la tabla 1 al 10: ")

for i in range(1,11):
    print(f"{i} x {tabla_del} = {i*int(tabla_del)}")


