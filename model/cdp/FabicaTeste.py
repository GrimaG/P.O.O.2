from model.cdp.FabricaCarro import Fabrica
from model.cdp.FabricaVip import FabricaVip

__author__ = 'Gustavo'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.carro = FabricaVip()
        self.assertEqual(Fabrica.criar_carro(self, "Vip"), self.carro )


if __name__ == '__main__':
    unittest.main()
