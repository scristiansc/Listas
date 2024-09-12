#Armar una lista con datos del usuario:
#Llenar una lista.
longitud = int(input("Cuantos estudiantes son?: "))

lista_del_man = []
#llenado de la lista
for i in range(0, longitud):
    elemento = input(f"Ingrese el estudiante #{i+1}: ")
    lista_del_man.append(elemento)

print("Terminado, siguiente...")

#Recorrido de la lista

for estudiante in lista_del_man:
    print(estudiante)