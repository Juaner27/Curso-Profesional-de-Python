# Metodos mas utilizados para Strings

lenguajes = "Python Ruby Java Rust C++ C"

# Metodo split divide por default con espacios 
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)
print(type(listado_lenguajes))

# separador de Strig se coloca como argumento en la función, guion por ejemplo: split("-")
lenguajes_2 = "Python//Ruby//Java//Rust//C++//C"

listado_lenguajes_2 = lenguajes_2.split("//")
print(listado_lenguajes_2)
print(type(listado_lenguajes_2))

"""
si se desa dividir por un numero de coincidencias especificas
se coloca un segundo argumento
split(//,2)
dividirá solo las primeras dos coincidencias
"""
# Metodo join crea un string a partir de una lista
lenguajes_3 = ["Python", "Ruby", "Java", "Rust", "C++", "C"]

string_lenguajes_3 = " ".join(lenguajes_3) # el separador se coloca como argumento, ejemplos "//", "-","*"
print(string_lenguajes_3)
print(type(string_lenguajes_3))


