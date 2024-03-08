def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    from datetime import datetime

    fecha_nacimiento = datetime(anno, mes, dia)
    fecha_actual = datetime.now()

    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    return "Su edad es: " + str(edad) + " años."

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
