uno, dos, tres, cuatro = 1, 2, 3, 4

print(uno)
print(dos)
print(tres)
print(cuatro)


# Creando tupla
numeros_tupla = (5, 6, 7, 8)
cinco, seis, siete, ocho =  numeros_tupla

# Cada valor será asignado a cada variable con respecto a los indices
print(cinco)
print(seis)
print(siete)
print(ocho)

# Si se desconoce cantidad de elementos en la tupla
cinco, seis, *resto_valores =  numeros_tupla
print(cinco)
print(seis)
print(resto_valores)

# * -> Crea lista de valores
# _ -> Para omitir valores
# *_ -> Omitir lista de valores

cinco, seis, _, ocho =  numeros_tupla
print(cinco)
print(seis)

print(ocho)

