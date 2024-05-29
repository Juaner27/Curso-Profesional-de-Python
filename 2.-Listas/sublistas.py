lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]
#                   0        1         2       3       4

# [start:end]
sub_lista = lista_cursos[0:3]
# del cero al 2, se exceptua el 3
print(sub_lista)

sub_lista = lista_cursos[0:4]
print(sub_lista)

# Obtener listas desde un indice hasta el final omitiendo el valor end
sub_lista = lista_cursos[1:]
print(sub_lista)
# [Start:] -> Obtenemos los últimos elementos de la lista

# [:end] -> Obtenemos los primeros elementos de la lista
sub_lista = lista_cursos[:4]
print(sub_lista)

# [Stat:end:skip] -> Para obtener una lista con saltos
sub_lista = lista_cursos[0:4:2]
print(sub_lista)

# [Start:end:-1] -> Obtener lista en orden inverso
sub_lista = lista_cursos[::-1]
print(sub_lista)



