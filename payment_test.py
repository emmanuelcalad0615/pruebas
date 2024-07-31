# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
import payment 


# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testPayment1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        compra = 850000
        tasa = 3.4
        plazo = 24
        cuota = 52377.50
        resultado = payment.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testPayment2(self):
        compra = 480000
        tasa = 0
        plazo = 48
        cuota = 10000

        resultado = payment.calcularCuota(compra, tasa, plazo)

        self.assertEqual(cuota, round(resultado, 2))

    """def testPayment3(self): 
        compra = 50000
        tasa = 12.4
        cuotas = 60
        resultado = "Error la tasa o puede superar el 100% anual"""""

           
    
    def testPayment4(self):
        compra = 90000
        tasa = 2.4
        plazo = 1
        cuota = 90000

        resultado = payment.calcularCuota(compra, tasa, plazo)

        self.assertEqual(cuota, round(resultado, 2))

        
unittest.main()