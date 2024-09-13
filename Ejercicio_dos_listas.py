# Dado un arreglo de números (numbers) y un número entero n,
# determine si n se encuentra en el arreglo. El programa debe imprimir
# True o False como corresponda.

longitud = int(input("¿Cuantos números va a ingresar?: "))

numeros = []

for i in range(longitud):
    lista_numeros = int(input(f"Ingrese el numero #{i+1}: "))
    numeros.append(lista_numeros)
print(f"Estos son tus numeros: ", numeros)

numero_random = int(input(f"Ingrese un numero: "))

resultado = False
for i in numeros:
    if numero_random == i:
        resultado = True
    
print(resultado)

