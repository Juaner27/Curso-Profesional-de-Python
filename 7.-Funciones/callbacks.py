promedio = lambda *args : sum(arg) / len(args)

aprobatorio =  lambda calificacion : calificacion >= 7

print(promedio(10, 10, 9, 8, 7))
print(aprobatorio(5))

# Combinando las dos funciones
def es_aprobatorio(calificacion):
    return calificacion >= 90

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if aprobatorio(promedio):
        print(f"Felicidades, aprobaste la materia con {promedio}.")
    else:
        print("No aprobaste la materia.")

mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)
