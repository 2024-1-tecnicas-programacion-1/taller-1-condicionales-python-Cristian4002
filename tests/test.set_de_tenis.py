import sys
from pathlib import Path
import unittest

from src.set_de_tenis import evaluar

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
class SetDeTenisTest(unittest.TestCase):
    def testProblema1(self):
        valorEsperado = "Datos incorrectos"
        valorActual = evaluar(-4, -5)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema2(self):
        valorEsperado = "Datos incorrectos"
        valorActual = evaluar(8, 9)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema3(self):
        valorEsperado = "Datos incorrectos"
        valorActual = evaluar(7, 7)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema4A(self):
        valorEsperado = "Gana el jugador A"
        valorActual = evaluar(7, 6)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema4B(self):
        valorEsperado = "Gana el jugador B"
        valorActual = evaluar(6, 7)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema5(self):
        valorEsperado = "Datos incorrectos"
        valorActual = evaluar(4, 7)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema6(self):
        valorEsperado = "Datos incorrectos"
        valorActual = evaluar(7, 2)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema7(self):
        valorEsperado = "Aún no termina"
        valorActual = evaluar(5, 5)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema8A(self):
        valorEsperado = "Gana el jugador A"
        valorActual = evaluar(7, 5)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema8B(self):
        valorEsperado = "Gana el jugador B"
        valorActual = evaluar(5, 7)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema9A(self):
        valorEsperado = "Gana el jugador A"
        valorActual = evaluar(6, 1)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema9B(self):
        valorEsperado = "Gana el jugador B"
        valorActual = evaluar(1, 6)
        self.assertEqual(valorEsperado, valorActual)

    def testProblema10(self):
        valorEsperado = "Aún no termina"
        valorActual = evaluar(2, 0)
        self.assertEqual(valorEsperado, valorActual)

    # Agrega tus otros casos de prueba aquí

if __name__ == '__main__':
    unittest.main()
