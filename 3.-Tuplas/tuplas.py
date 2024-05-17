cursos = ("Python", "Flask", "Django", "Rails", "MongoDB")
#           0           1       2          3       4

primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(primer_curso)

# Sub_tuplas [Start:end]

sub_tupla = cursos[0:3]
print(sub_tupla)


"""
Tienen el mismo compartamiento que las listas respecto a los indices
[Start:end:skip] -> Tupla con salto de indice
[:end] -> Detalle los primeros elementos de la tupla hasta un indice especifico
[:] -> Sub_tupla con todos los elementos de la tupla original
Las tuplas no podran cambiarse mas adelante del proyecto
"""
