import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test2000Enero1(self):
        valorEsperado = "Su edad es: 24 años."
        valorActual = evaluar(1, 1, 2000)
        self.assertEqual(valorEsperado, valorActual)

    def test1985Febrero10(self):
        valorEsperado = "Su edad es: 39 años."
        valorActual = evaluar(10, 2, 1985)
        self.assertEqual(valorEsperado, valorActual)

    def test2005Diciembre4(self):
        valorEsperado = "Su edad es: 18 años."
        valorActual = evaluar(4, 12, 2005)
        self.assertEqual(valorEsperado, valorActual)

    # Agrega tus otros casos de prueba aquí
    # TODO: Agrega tus otros casos de prueba aquí
    

if __name__ == '__main__':
    unittest.main()
