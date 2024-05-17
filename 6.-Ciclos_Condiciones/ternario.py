calificacion = 10
color = None

if calificacion >= 7:
    color = "Verde"
else:
    color = "Rojo"

print(calificacion, color)

# En una sola linea
calificacion = 5


#       cumple                          no cumple
color = "Verde" if calificacion >= 7 else "Rojo"

print(calificacion, color)

