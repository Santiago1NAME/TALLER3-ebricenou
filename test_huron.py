import unittest
from huron import Huron

class TestHurones(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron()
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        huron = Huron()
        self.assertEqual(huron.calcular_flete(23, 21), 483)

if __name__ == "__main__":
    unittest.main()