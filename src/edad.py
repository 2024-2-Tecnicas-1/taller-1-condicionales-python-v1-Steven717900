from datetime import datetime

def evaluar(dia, mes, anno):

        fecha_actual = datetime.now()
        fecha_nacimiento = datetime(anno, mes, dia)
        
        edad = fecha_actual.year - fecha_nacimiento.year
        
        if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        
        respuesta = f"Usted tiene {edad} años"
        return respuesta
    

if _name_ == '_main_':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end=" ")
    dia = int(input())
    print("Mes:", end=" ")
    mes = int(input())
    print("Año:", end=" ")
    anno = int(input())
    
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
