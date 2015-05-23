from model.cdp.AbstrcEstiloCarro import Estilo
from model.cdp.AbstrcFabricaCarro import FabricaCarro
from model.cdp.AbstrcTamanhoCarro import Tamanho
from model.cdp.Medio import Medio
from model.cdp.Vip import Vip

__author__ = 'Gustavo'

class FabricaVip(FabricaCarro):
    def __init__(self):
        self.tamanho = Tamanho()
        self.tipo = Estilo()
        self.criarCarro()

    def criarCarro(self):
        self.tamanho = Medio()
        self.tipo = Vip()
