diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

print("a" in diccionario)

valor = diccionario["d"]
print(valor)

# Metodo get

valor = diccionario.get("c", "la llave no existe en el dict.")

print(valor)


# Metodo setdefault
valor = diccionario.setdefault("c", 5)

print(valor)
print(diccionario)

