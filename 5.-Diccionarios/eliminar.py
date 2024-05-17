# Metodo del
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

print(len(diccionario))

del diccionario["a"]

print(diccionario)
print(len(diccionario))


# Metodo pop
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

print(len(diccionario))

del diccionario["a"] # 1
valor = diccionario.pop("b") # 2
print(valor)


print(diccionario)
print(len(diccionario))


# Metoo clear para eliminar todos los elementos de los diccionarios
diccionario.clear()
print(diccionario)
