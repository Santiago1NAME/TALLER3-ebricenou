import unittest
from boa import BoaConstrictor

class TestBoas(unittest.TestCase):
    def test_hacer_sonido(self):
        boa = BoaConstrictor()
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        boa = BoaConstrictor()
        self.assertEqual(boa.calcular_flete(20, 15.1), 302)

    def test_alimentar(self):
        boa = BoaConstrictor()
        for _ in range(10):
            boa.alimentar()
        with self.assertRaises(ValueError):
            boa.alimentar()

if __name__ == "__main__":
    unittest.main()