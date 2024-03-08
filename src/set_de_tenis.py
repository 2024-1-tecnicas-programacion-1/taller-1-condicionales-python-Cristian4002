def evaluar(num_victorias_a, num_victorias_b):
    # Problema 1: No pueden ser menores que 0
    if num_victorias_a < 0 or num_victorias_b < 0:
        return "Datos incorrectos"

    # Problema 2: No pueden ser mayores que 7
    if num_victorias_a > 7 or num_victorias_b > 7:
        return "Datos incorrectos"

    # Problema 3: No pueden ambos ser iguales a 7
    if num_victorias_a == 7 and num_victorias_b == 7:
        return "Datos incorrectos"

    # Problema 4: si el resultado es 6-7 o 7-6
    if (num_victorias_a == 7 and num_victorias_b == 6) or (num_victorias_a == 6 and num_victorias_b == 7):
        if num_victorias_a == 7:
            return "Gana el jugador A"
        else:
            return "Gana el jugador B"

    # Problema 5: No pueden ser igual a 7 y tener una diferencia mayor a 2 con el otro
    if (num_victorias_a == 7 and num_victorias_b > 5) or (num_victorias_b == 7 and num_victorias_a > 5):
        return "Datos incorrectos"

    # Problema 6: Si uno es igual a 7, el otro debe ser 5 o 6
    if (num_victorias_a == 7 and not (num_victorias_b == 5 or num_victorias_b == 6)) \
            or (num_victorias_b == 7 and not (num_victorias_a == 5 or num_victorias_a == 6)):
        return "Datos incorrectos"

    # Problema 7: Si ambos son iguales, el partido no ha terminado
    if num_victorias_a == num_victorias_b:
        return "Aún no termina"

    # Problema 8: Si el resultado es 5 - 7 o 7 - 5
    if (num_victorias_a == 7 and num_victorias_b == 5) or (num_victorias_a == 5 and num_victorias_b == 7):
        if num_victorias_a == 7:
            return "Gana el jugador A"
        else:
            return "Gana el jugador B"

    # Problema 9: Si alguno llega a 6 con una diferencia de dos puntos
    if num_victorias_a == 6 or num_victorias_b == 6:
        if abs(num_victorias_a - num_victorias_b) >= 2:
            if num_victorias_a == 6:
                return "Gana el jugador A"
            else:
                return "Gana el jugador B"

    # Si ninguno de los problemas anteriores se ha encontrado, el juego está en progreso
    return "Aún no termina"

def main():
    num_victorias_a = int(input("Los juegos ganados por A: "))
    num_victorias_b = int(input("Los juegos ganados por B: "))

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)

if __name__ == "__main__":
    main()
