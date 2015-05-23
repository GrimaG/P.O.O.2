from model.cdp.FabricaBasico import FabricaBasico
from model.cdp.FabricaCarro import Fabrica
from model.cdp.FabricaLuxo import FabricaLuxo
from model.cdp.FabricaVip import FabricaVip

__author__ = 'Gustavo'

import unittest


class MyTestCase(unittest.TestCase):
    def teste_vip(self):
        self.carro = FabricaVip()
        self.assertEqual(Fabrica.criar_carro(self, "Vip"), self.carro )

    def teste_luxo(self):
        self.carro = FabricaLuxo()
        self.assertEqual(Fabrica.criar_carro(self, "Luxo"), self.carro )

    def teste_basico(self):
        self.carro = FabricaBasico()
        self.assertEqual(Fabrica.criar_carro(self, "Basico"), self.carro )

if __name__ == '__main__':
    unittest.main()
