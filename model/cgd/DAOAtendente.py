from model.cdp.Atendente import Atendente
from model.cdp.Endereco import Endereco
__author__ = 'Gustavo'

class DAOAtendente:

    def gravar(self, atendente):
        f = open('atendente.txt', 'a')
        f.write('\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (atendente.nome, atendente.telefone, atendente.cpf, atendente.endereco.cep, atendente.endereco.cidade, atendente.endereco.numero, atendente.endereco.rua,  atendente.endereco.referencia ))
        f.close()

    def puxar(self):
        list = []
        atendente = Atendente()
        f = open('atendente.txt', 'r')
        f.readline()
        while 1:
             atendente.nome = f.readline()
             atendente.telefone = f.readline()
             atendente.cpf = f.readline()
             atendente.endereco.cep = f.readline()
             atendente.endereco.cidade = f.readline()
             atendente.endereco.numero = f.readline()
             atendente.endereco.rua = f.readline()
             atendente.endereco.referencia = f.readline()
             list.append(atendente)

             if not f.readline():
                 break

        f.close()
        return list