from model.cdp.AbstrcFabricaCarro import FabricaCarro
from model.cdp.Endereco import Endereco

__author__ = 'Gustavo'

class Viagem():
    def __init__(self, estilo):
        self.enderecoOrigem = Endereco()
        self.cliente = ""
        self.qtdPessoa = 0
        self.endDestino = 0
        self.status = ""
        self.Taxi = FabricaCarro(estilo)
    pass
