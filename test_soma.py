import unittest
from app import app, index

class SomaTest(unittest.TestCase):

    def test_soma_numeros_positivos(self):
        with app.test_client() as test_client:
            response = test_client.post('/', data=dict(num1=5, num2=3))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Resultado: 8', response.data)

    def test_soma_numeros_negativos(self):
        with app.test_client() as test_client:
            response = test_client.post('/', data=dict(num1=-2, num2=-4))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Resultado: -6', response.data)

    def test_soma_com_valor_nao_numerico(self):
        with app.test_client() as test_client:
            response = test_client.post('/', data=dict(num1='a', num2=3))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Por favor, insira apenas numeros.', response.data)

if __name__ == '__main__':
    unittest.main()