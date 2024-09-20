# Dado un arreglo, indique si es simétrico, un arreglo es simétrico si
# siendo longitud par los números de la primera mitad son iguales al
# inverso de la otra mitad.
# ○ Ejemplo: El arreglo [1,2,3,3,2,1] es simétrico.
# En caso de que la longitud sea impar, se ignorará el elemento central
# y se seguirá la misma lógica anterior.
# ○ Ejemplo: El arreglo [3,5,7,8,7,5,3] es de longitud impar y es
# simétrico.


longitud = int(input("Ingrese la cantidad de numeros: "))
mitad = longitud // 2 

lista = []

es_simetrico = True

for i in range(longitud):
    numeros = int(input(f"Ingrese el numero {i+1} de la lista: "))
    lista.append (numeros)
for i in range(mitad):
    if lista [i] != lista [longitud - i - 1]:
        es_simetrico = False
        break

print(lista)

if es_simetrico:
    print("La lista es simetrica")
else:
    print("El arreglo no es simetrico")
