from model.cdp.AbstrcEstiloCarro import Estilo
from model.cdp.AbstrcFabricaCarro import FabricaCarro
from model.cdp.AbstrcTamanhoCarro import Tamanho
from model.cdp.Grande import Grande
from model.cdp.Luxo import Luxo

__author__ = 'Gustavo'

class FabricaLuxo(FabricaCarro):
    def __init__(self):
        self.tamanho = Tamanho()
        self.tipo = Estilo()
        self.criarCarro()

    def criarCarro(self):
        self.tamanho = Grande()
        self.tipo = Luxo()
