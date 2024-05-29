def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

print(centigrados_a_farhenheit(10))
print(centigrados_a_farhenheit(-1))
print(centigrados_a_farhenheit(8))

# Creando una variable para la función
mi_funcion = centigrados_a_farhenheit

print(type(mi_funcion))

print(mi_funcion(10))

# Función lambda son anonimas

funcion_grados = lambda grados : grados * 1.8 + 32

# lambda <parámetros> : <Cuerpo de la función>
print(funcion_grados(10))

"""
sin_parametros =  lambda : True

parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3

asterisco = lambda *args, **kwargs: len(args) + len(kwargs)
print(asterisco)

 """
 