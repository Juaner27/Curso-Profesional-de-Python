# Scope
animal = "León" # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    animal = "Ballena" # Variable Local
    tipo = "Mamifero" # Variable Local
    
    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))

# Modificar el valor de la variable Global usando la palabra global
animal = "León" # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    global animal
    animal = "Ballena" # Variable Local
    tipo = "Mamifero" # Variable Local
    
    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))
