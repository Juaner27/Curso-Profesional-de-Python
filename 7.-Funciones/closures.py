e = "e" # variable Global

def funcion_principal():
    a = "a"  # Variable Local con scope superior con mayor alcance
    b = "b"


    def funcion_anidada():
        c = "c"  # Variable Local
        
        nonlocal b  # Para usar una variable local de un nivel superior
        b = "Cambio d valor"

        print(a)
        print(b)
        print(id(b))

        print(e)
        
    
    funcion_anidada()
    print(c)  # da error porque esta dentro de un scope menor
    
    print(b)
    print(id(b))

funcion_principal()
