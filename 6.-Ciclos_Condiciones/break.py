titulo_curso = "Curso profesional de Python"

# finaliza la ejecución del ciclo
for caracter in titulo_curso:
    
    if caracter == "P":
        break

    print(caracter)

# se salta a la siguiente iteración
for caracter in titulo_curso:
    
    if caracter == " ":
        continue

    print(caracter)
