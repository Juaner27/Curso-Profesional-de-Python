def suma(numero_uno, numero_dos):

    resultado = numero_uno + numero_dos
    print(resultado)

numero_uno = int(input("Ingresa el primer numero entero: "))
numero_dos = int(input("Ingresa el segundo numero entero: "))

suma(numero_uno, numero_dos)


def suma(n1, n2):

    resultado = n1 + n2
    print(resultado)

numero_uno = int(input("Ingresa el primer numero entero: "))
numero_dos = int(input("Ingresa el segundo numero entero: "))

suma(numero_uno, numero_dos)

# Palabra reservada return
def suma(n1, n2):
    resultado = n1 + n2
    return resultado

numero_uno = int(input("Ingresa el primer numero entero: "))
numero_dos = int(input("Ingresa el segundo numero entero: "))

resultado = suma(numero_uno, numero_dos)
print(resultado)

# Reduciendo código
def suma(n1, n2):
    return = n1 + n2, "La función retorna 2 valores"
    
numero_uno = int(input("Ingresa el primer numero entero: "))
numero_dos = int(input("Ingresa el segundo numero entero: "))

# Podemos omitir el segundo valor "resultado, _"
resultado, mensaje = suma(numero_uno, numero_dos)
print("El resultado es: ", resultado)


