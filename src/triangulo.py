def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis

    if a < (b + c) and b < (a + c) and c < (a + b):
        if (a == b and a != c) or (a == c and b != c) or (b == c and a != b):
            respuesta = "El triángulo es isósceles"
        elif a != b and b != c and a != c:
            respuesta = "El triángulo es escaleno"
        elif a == b and b == c:
            respuesta = "El triángulo es equilátero"
    else:
        respuesta = "No es un triángulo válido"
    
    return respuesta

if _name_ == '_main_':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
