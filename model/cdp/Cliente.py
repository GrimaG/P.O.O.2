from model.cdp.AbstrcPessoa import Pessoa

__author__ = 'Gustavo'
class Cliente(Pessoa):
    def __init__(self):
        super(Cliente, self).__init__()
        self.email = " "
