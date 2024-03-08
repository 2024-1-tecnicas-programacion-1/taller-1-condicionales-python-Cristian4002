def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    imc = peso / (estatura * estatura)
    if edad < 45:
        if imc < 22.0:
            return "Riesgo bajo."
        else:
            return "Riesgo medio."
    else:
        if imc < 22.0:
            return "Riesgo medio."
        else:
            return "Riesgo alto."

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
