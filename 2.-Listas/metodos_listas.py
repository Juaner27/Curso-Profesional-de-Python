lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# Ordenar listas con metodo sort ascendente
lista.sort()
print(lista)

# Ordenar listas con metodo sort descendente
lista.sort(reverse=True)
print(lista)

# Identificar el numero mayor y menor
lista.sort()
print(lista[0])     # min
print(lista[-1])    # max

# Con funciones min - max

print(min(lista))
print(max(lista))


# Buscar un elemento en especifico
print(10 in lista)
print(5 in lista)
# El resultado es un valor booleano

# Confirmar que no se encuenta en el listado
print(10 not in lista)
print(5 not in lista)

# Obtener el indice de un elemento con metodo index
print(5 in lista)
index = lista.index(5)
print(lista)
"""
Va a retornar el primer indice de izquierda a derecha
en el caso de existir en varios indices de la lista
"""