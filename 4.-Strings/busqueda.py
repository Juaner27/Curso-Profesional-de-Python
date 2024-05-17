titulo_curso = "Curso profesional de Python"


# Buscar la cantidad de veces que existe un string dentro de otro
contador = titulo_curso.count("Python")
print(contador)


# Puede buscarse un solo caracter
contador = titulo_curso.count("o")
print(contador)

print("Python" in titulo_curso)

# standarizar el string a minusculas con el Metodo lower
print("Python" in titulo_curso.lower())

# standarizar el string a mayusculas con el Metodo uper
print("Python" in titulo_curso.uper())

# También podemos negar
print("CódigoFacilito" not in titulo_curso.lower())

# Metodo starswith permite conocer si un string esta al inicio de otro string
print(titulo_curso.startswith("Curso"))

# Metodo endswith permite conocer si un string esta al final de otro string
print(titulo_curso.endswith("Python"))

