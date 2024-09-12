# Dada dos listas (lista1 y lista2),de como resultado
# dos listas resultantes: una de la suma entre la
# lista1 y lista2,y otra de la resta.

#prueba de escritorio--->pedir la longitud de las listas(debe ser la misma)
#Pedir los numeros de la lista1 y de la lista2
#Arrojar una lista de la suma de ambas y otra lista con la resta

longitud = int(input("Cuantos numeros tiene la lista?: "))

lista_uno = []
lista_dos = []

for i in range(longitud):
    numeros_lista_uno = int(input(f"Ingrese el numero #{i+1}: "))
    lista_uno.append(numeros_lista_uno)

for numero in lista_uno:
    print(numero)


for i in range(0,longitud):
    numeros_lista_dos = int(input(f"Ingrese el numero #{i+1} de la lista #2: "))
    lista_dos.append(numeros_lista_dos)

for numero in lista_dos:
    print(numero)

lista_suma = []
lista_resta = []

for i in range(longitud):
    lista_suma.append(lista_uno[i] + lista_dos[i])
    lista_resta.append(lista_uno[i] - lista_dos[i])

print("Resultado lista suma: ")
print(lista_suma)

print("Resultado lista resta: ")
print(lista_resta)
    
    