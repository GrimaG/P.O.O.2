from model.cdp.AbstrcPessoa import Pessoa

__author__ = 'Gustavo'

class Motorista(Pessoa):
    def __init__(self):
        super(Motorista, self).__init__()
        self.cnh = ""