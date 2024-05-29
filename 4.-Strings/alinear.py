# Justificar texto de un string
mensaje = "Hola mundo!"
print(mensaje)

# Metodo ljust -> Justificar a la izquierda

mensaje = mensaje.ljust(20)

print(mensaje, ".")

# Metodo rjust -> Justificar a la derecha
mensaje = mensaje.rjust(20)

print(mensaje, ".")

# Metodo center -> Justificar al centro
mensaje = mensaje.center(20)

print(mensaje, ".")
