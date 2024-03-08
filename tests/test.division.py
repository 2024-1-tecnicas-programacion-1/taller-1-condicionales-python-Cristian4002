import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    
    # TODO: Agrega tus otros casos de prueba aquí
    def testDivisionExacta(self):
        valorEsperado = "La división es exacta. \n" \
                        + "Cociente: 2\n" \
                        + "Residuo: 0"
        valorActual = evaluar(14, 7)
        self.assertEqual(valorEsperado, valorActual)

    def testDivisionNoExacta(self):
        valorEsperado = "La división no es exacta. \n" \
                        + "Cociente: 0\n" \
                        + "Residuo: 1"
        valorActual = evaluar(1, 4)
        self.assertEqual(valorEsperado, valorActual)


if __name__ == '__main__':
    unittest.main()
