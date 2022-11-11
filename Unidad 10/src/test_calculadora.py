import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(calculadora.sumar(2, 3), 5)
        self.assertEqual(calculadora.sumar(6, 13), 19)
        self.assertEqual(calculadora.sumar(-5, -4), -9)
        with self.assertRaises(TypeError):
            calculadora.sumar(5, 'hello')

    def test_restar(self):
        self.assertEqual(calculadora.restar(4, 1), 3)
        self.assertEqual(calculadora.restar(3, -2), 5)
        self.assertEqual(calculadora.restar(4, 6), -2)
        with self.assertRaises(TypeError):
            calculadora.restar(8, 'asd')

    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicar(0, 6), 0)
        self.assertEqual(calculadora.multiplicar(1, 3), 3)
        self.assertEqual(calculadora.multiplicar(7, -8), -56)
        with self.assertRaises(TypeError):
            calculadora.multiplicar(1, 'asd')

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(5, 5), 1)
        self.assertEqual(calculadora.dividir(12, 4), 3)
        with self.assertRaises(TypeError):
            calculadora.dividir(3, 'bye')
        # self.assertEqual(calculadora.dividir(3, 0), None)
        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(6, 0)
