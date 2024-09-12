#Array,Listas
notas = [3.7, 4.2, 5.0, 2.5]


#1ra forma: Recorrer los elementos como tal,
#es decir, 'i' sera cada elemento de la lista.
for i in notas:
    print(f"Tienes esta nota: {i}")
for nota in notas:
    print(f"Tienes esta nota: {nota}")

#2da forma: Recorrer las posiciones/indices como tal,
#es decir, 'i' sera cada posicion de los elementos de la lista.
for i in range (len(notas)):
    print (f"Tu nota # {i+1} es {notas[i]}")