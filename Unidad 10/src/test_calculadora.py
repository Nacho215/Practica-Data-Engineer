import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(calculadora.sumar(2, 3), 5)
        self.assertEqual(calculadora.sumar(-4, 8, -2), 2)
        self.assertEqual(calculadora.sumar(3, -15, 8, 0, -3), -7)
        self.assertEqual(calculadora.sumar(1, [3, 2], 9), None)
        self.assertEqual(calculadora.sumar(3, 6, '10'), None)

    def test_restar(self):
        self.assertEqual(calculadora.restar(6, 2), 4)
        self.assertEqual(calculadora.restar(8, -5, -4), 17)
        self.assertEqual(calculadora.restar(-5, 11, -4, 1, -3), -10)
        self.assertEqual(calculadora.restar(4, {-4, 1}, -7), None)
        self.assertEqual(calculadora.restar({3: 2}, 4, '-8'), None)

    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicar(0, 6), 0)
        self.assertEqual(calculadora.multiplicar(1, 3), 3)
        self.assertEqual(calculadora.multiplicar(7, -8, 6, 2), -672)
        self.assertEqual(calculadora.multiplicar(1, '3', 4, -2), None)
        self.assertEqual(calculadora.multiplicar(7, -8, 0, -1, {2, -4}), None)

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(5, 5), 1)
        self.assertEqual(calculadora.dividir(-12, 4), -3)
        self.assertEqual(calculadora.dividir(128, 2, 2, 2, 2, 2), 4)
        self.assertEqual(calculadora.dividir(12, 0, -2), None)
        self.assertEqual(calculadora.dividir(5, '4', -2, [1, 2]), None)


if __name__ == "__main__":
    unittest.main()
