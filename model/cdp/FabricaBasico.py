from model.cdp.AbstrcEstiloCarro import Estilo
from model.cdp.AbstrcFabricaCarro import FabricaCarro
from model.cdp.AbstrcTamanhoCarro import Tamanho
from model.cdp.Basico import Basico
from model.cdp.Pequeno import Pequeno

__author__ = 'Gustavo'
class FabricaBasico(FabricaCarro):
    def __init__(self):
        self.tamanho = Tamanho()
        self.tipo = Estilo()
        self.criarCarro()

    def criarCarro(self):
        self.tamanho = Pequeno()
        self.tipo = Basico()
