from model.cdp.Atendente import Atendente
__author__ = 'Gustavo'

class DAOAtendente:

    def gravar(self, atendente):
        f = open('atendente', 'a')
        f.write('%s\n%s\n%s\n%s\n')
        f.close()
    def puxar(self):
        f = open('atendente', 'r')
        while 1:
             linha1 = f.readline()
             linha2 = f.readline()
             linha2 = f.readline()
             linha2 = f.readline()
             if not line:
                 break
        f.close()