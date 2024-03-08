import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.letra_o_numero import evaluar

class TestLetraONumero(unittest.TestCase):
    def testEsNumero(self):
        valorEsperado = "El caracter ingresado es un número."
        valorActual = evaluar('5')
        self.assertEqual(valorEsperado, valorActual)

    def testEsLetraMinuscula(self):
        valorEsperado = "El caracter ingresado es una letra minúscula."
        valorActual = evaluar('c')
        self.assertEqual(valorEsperado, valorActual)

    def testEsletraMayuscula(self):
        valorEsperado = "El caracter ingresado es una letra mayúscula."
        valorActual = evaluar('G')
        self.assertEqual(valorEsperado, valorActual)

    def testNoEsLetraNiNumero(self):
        valorEsperado = "El caracter ingresado no es ni letra ni número."
        valorActual = evaluar('$')
        self.assertEqual(valorEsperado, valorActual)

    # TODO: Agrega tus otros casos de prueba aquí
    

if __name__ == '__main__':
    unittest.main()
