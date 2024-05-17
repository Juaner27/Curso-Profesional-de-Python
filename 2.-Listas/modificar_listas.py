#                   0         1         2       3       4
lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]
#                  -5        -4        -3      -2      -1

lista_cursos_2 = ["c","C++","Docker"]

# Obtener longitud de lista
print(len(lista_cursos))


# Agregar elementos a la lista
lista_cursos.append("MongoBD")
lista_cursos.append("C#")
lista_cursos.append("JavaScript")

# Agregar un indice en particular
lista_cursos.insert(1,"Rails")
lista_cursos.insert(0,"PyGame")

# Añadir elementos de otra lista, combinar los elementos de varias listas
lista_cursos.extend(lista_cursos_2)


print(lista_cursos)
# Eliminando elementos de lista
lista_cursos.remove("MongoBD") # Por nombre de elemento
del lista_cursos[0]            # Por indice de lista


print(lista_cursos)
print(len(lista_cursos))

# Eliminar todos los elementos de la lista
lista_cursos.clear()
print(lista_cursos)
print(len(lista_cursos))
