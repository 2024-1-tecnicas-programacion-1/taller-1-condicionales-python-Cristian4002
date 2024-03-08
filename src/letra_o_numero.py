def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    if caracter.isalpha():
        if caracter.isupper():
            return "El caracter ingresado es una letra mayúscula."
        else:
            return "El caracter ingresado es una letra minúscula."
    elif caracter.isdigit():
        return "El caracter ingresado es un número."
    else:
        return "El caracter ingresado no es ni letra ni número."

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
