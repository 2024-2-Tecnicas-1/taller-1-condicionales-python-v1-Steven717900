def evaluar(peso, estatura, edad):
        # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    IMC = peso / (estatura ** 2)
    if edad < 45:
        if IMC < 22.0:
            respuesta = "bajo"
        else:
            respuesta = "medio"
    else:
        if IMC < 22.0:
            respuesta = "medio"
        else:
            respuesta = "alto"
    
    return respuesta

if _name_ == '_main_':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
