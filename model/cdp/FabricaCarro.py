from model.cdp.AbstrcFabricaCarro import FabricaCarro
from model.cdp.FabricaBasico import FabricaBasico
from model.cdp.FabricaLuxo import FabricaLuxo
from model.cdp.FabricaVip import FabricaVip

__author__ = 'Gustavo'
class Fabrica:
    def __init__(self, estilo):
        self.carro = FabricaCarro()

    def criar_carro(self,estilo):
        if estilo == "Vip":
            self.carro= FabricaVip()
        if estilo == "Luxo":
           self.carro= FabricaLuxo()
        if estilo == "Basico":
            self.carro = FabricaBasico()
        return self.carro