__author__ = 'Gustavo'
class Notifica():

        def __new__(cls, *args, **kwargs):
            if not hasattr(cls, '_instance'):
                 cls._instance = super(Notifica, cls).__new__(cls, *args, **kwargs)
            return cls._instance

        def atualiza(self, viagem, list):
            for elemento in list:
                if elemento == viagem:
                    self.elemento = viagem
            return list

        def verifica(self, list):
            for viagem in list:
                if viagem == "aberto":
                    return viagem
            return 0