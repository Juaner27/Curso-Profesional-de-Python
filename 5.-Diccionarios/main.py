diccionario = {}
diccionario = dict{}

#{ llave: el valor el cual queremos asociar. }
diccionario = {"total":55}

diccionario = {"total": 55, "descuento": True, "subtotal": 15}

diccionario = {"total": 55, 10: "Curso de Python", (1,2,3): True}

# Llaves

# Un string ("total")
# Un número entero (10)
# Una tupla que almacena números enteros (1,2,3)

usuario = {
    "nombre": "Nombre del usuario",
    "edad": 23,
    "curso": "Curso de Python",
    "skills":{
        "programacion"  : True,
        "base_de_datos" : False
    },
    "medallas": ["basico", "intermedio"]
}

# Creación del diccionario
diccionario = dict()

# Agregar nueva llave valor
diccionario["usuario"] = "Juan"

# Actualizar valor mediante una llave
diccionario["usuario"] = "Juan_eaz"

# Obtener valor mediante una llave
print(diccionario["usuario"])

>>> diccionario = {"Juan": 1, "Eduardo": 2, "Carlos": 3, "Wilber": 4}

>>> diccionario.keys()
dict_values([1, 2, 3, 4])

>>> for key, value in diccionario.items():
...     print(key, value)
...
Juan 1
Eduardo 2
Carlos 3
Wilber 4

# Ejemplo 
usuario = {
    "name": "Juan Ernesto"
    "age": 40
    "job": "CódigoFacilito"
}


calificaciones = usuario.get("calificaciones",[])
if calificaciones:

    for calificaciones in calificaciones:
        print(calificaciones)


# dict.comprensation

usuario = ["Juan", "Eduardo", "Cralos", "Wilber"]

diccionario = {usuario:position +1
                        for position, usuario in enumarate(usuarios)
}

print(diccionario)


