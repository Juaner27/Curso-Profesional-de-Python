#                   0         1         2       3       4
lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]
#                  -5        -4        -3      -2      -1

print(lista_cursos)

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_cursos = lista_cursos[1]
print(segundo_cursos)

ultimo_curso = lista_cursos[4]
print(ultimo_curso)

ultimo_curso = lista_cursos[-3]
print(ultimo_curso)

"""
Trabando con indices negativos:
ultimo_curso = lista_curso[-1]
print(ultimo_curso)

positivos de izquierda a derecha desde cero 
negativos de derecha a izquierda desde -1
"""

# Remplazando valores de la lista con indices

lista_cursos[4] = "Rust"
print(lista_cursos)

