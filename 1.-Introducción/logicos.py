# and: todas las condiciones deben ser verdaderas para que el resultado sea True

resultado_final = True and True and True
print(resultado_final)

resultado_final = True and True and False
print(resultado_final)

resultado_final = True and True and 10 < 100
print(resultado_final)


# or: al menos una condicion debe ser verdadera para que el resultado sea True

resultado_final = True or False or False
print(resultado_final)

resultado_final = False or False or False
print(resultado_final)

resultado_final = False or False or 10 < 100
print(resultado_final)


# not
# permite negar un valor booleano

resultado_final = not True
print(resultado_final)
# verdadero lo convierte a falso y viceversa


# Combinación de operadores logicos
# and, or, not
                #true and true
resultado_final = True and ( False or 50 > 10 )
print(resultado_final)
