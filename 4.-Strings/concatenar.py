# Generar nuevos string a partir de otros 

nombre = "Juan Ernesto"
apellido = "Arteaga"

"""
# Usando el operador +
nombre_completo = "Mr. " + nombre + " " + apellido

print(nombre_completo)
"""

"""
# Usando %s para crear un string de otro string base
nombre_completo = "Mr. %s %s." %(nombre, apellido)
print(nombre_completo)
"""

"""
# Metodo Format respecto a su posición
nombre_completo = "Mr. {} {} {}." .format(nombre, apellido, "Santeliz")
print(nombre_completo)


# Metodo Format respecto a su nombre
nombre_completo = "Mr. {nombre} {primer_apellido} {segundo_apellido}." .format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido="Santeliz"
)
print(nombre_completo)
"""
# Metodo FString con interpolación
nombre_completo = f"Mr.{nombre} {apellido} {"Santeliz"} {10 * 20}"
print(nombre_completo)
