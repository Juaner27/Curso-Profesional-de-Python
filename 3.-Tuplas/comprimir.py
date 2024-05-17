lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

resultado = zip(tupla, lista) # Retorna un objeto tipo zip

print(resultado)
print(type(resultado))

resultado = tuple(resultado)
print(resultado)
print(type(resultado))

lista_2 = [100, 200, 300, 400, 500]
tupla_2 = (1000, 2000, 3000, 4000, 5000)
resultado = zip(tupla, lista, lista_2, tupla_2)
resultado = tuple(resultado)
print(resultado)
print(type(resultado))

"""
Si una lista o una tupla posee una cantidad mayor de elementos
estos son omitidos 
"""