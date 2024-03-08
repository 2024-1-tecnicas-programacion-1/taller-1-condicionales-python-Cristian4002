import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.imc import evaluar

class TestIMC(unittest.TestCase):
    def testBajo(self):
        valorEsperado = "Riesgo bajo."
        valorActual = evaluar(50, 1.7, 20)
        self.assertEqual(valorEsperado, valorActual)

    def testMedio(self):
        valorEsperado = "Riesgo medio."
        valorActual = evaluar(45, 1.5, 48)
        self.assertEqual(valorEsperado, valorActual)

    def testAlto(self):
        valorEsperado = "Riesgo alto."
        valorActual = evaluar(64, 1.6, 45)
        self.assertEqual(valorEsperado, valorActual)

    
    # TODO: Agrega tus otros casos de prueba aquí
    

if __name__ == '__main__':
    unittest.main()
