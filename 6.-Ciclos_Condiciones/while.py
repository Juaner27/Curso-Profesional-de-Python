contador = 1

# Cuando no sabemos cuantas iteraciones se van realizar
while contador <= 10:
    print(contador)

    contador =  contador + 1

numero = 123456789
contador_digitos = 0

while numero >= 1:
   # contador_digitos = contador_digitos + 1
    contador_digitos += 1
    numero =  numero / 10
else:
   # print("Fin del ciclo while")
    print(contador_digitos)
