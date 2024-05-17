def area_circulo(radio, pi):
    return pi * (radio ** 2)

resultado = area_circulo(10, 3.14)
print(resultado)

# Definiendo el valor por default de un parametro
def area_circulo(radio, pi=3.14): # sin espacios, todo va unido para difinir el valor del parametro
    return pi * (radio ** 2)

resultado = area_circulo(10, 3.141592) # se puede asignar valor al parametro aunque este definido por default
print(resultado)


resultado = area_circulo(pi=3.141592, radio=10) # se puede asiganar valor respecto de sus nombres
print(resultado)
