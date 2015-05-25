from model.cdp.Motorista import Motorista

__author__ = 'Gustavo'

class DAOTaxista:

     def gravar(self, motorista):
         f = open('motorista.txt', 'a')
         f.write('\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (motorista.nome, motorista.telefone, motorista.cpf, motorista.endereco.cep, motorista.endereco.cidade, motorista.endereco.numero, motorista.endereco.rua,  motorista.endereco.referencia, motorista.cnh ))
         f.close()

     def puxar(self):
        list = []
        motorista = Motorista()
        f = open('motorista.txt', 'r')
        f.readline()
        while 1:
             motorista.nome = f.readline()
             motorista.telefone = f.readline()
             motorista.cpf = f.readline()
             motorista.endereco.cep = f.readline()
             motorista.endereco.cidade = f.readline()
             motorista.endereco.numero = f.readline()
             motorista.endereco.rua = f.readline()
             motorista.endereco.referencia = f.readline()
             motorista.cnh = f.readline()
             list.append(motorista)

             if not f.readline():
                 break

        f.close()
        return list