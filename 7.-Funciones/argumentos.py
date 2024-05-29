# print("string", 10, 14.5, True)

def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10, 10, 5, 7, 10])
print(resultado)


# usando * para n cantidad de argumentos
def promedio(*listado):
    print(type(listado))

    return sum(listado) / len(listado)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)



# por convención de la comunidad Python
def promedio(*args):
    print(type(args))

    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)


def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)


# Usando doble **
def promedio(*args): # Tupla
    return sum(args) / len(args)


def usuarios(**kwargs): # Diccionario
    print(kwargs)
    print(type(kwargs))
    
usuarios(Ernesto=[10, 10, 8], Juan=[10, 9, 9])

#def combinacion(p1, p2, *args, **kwargs, p5=500):
def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, cody=True, curso="Python")



