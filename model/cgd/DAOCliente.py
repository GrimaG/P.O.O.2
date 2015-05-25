from model.cdp.Cliente import Cliente
__author__ = 'Gustavo'

class DAOCliente:
    def gravar(self, cliente):
        f = open('cliente.txt', 'a')
        f.write('\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (cliente.nome, cliente.telefone, cliente.cpf, cliente.endereco.cep, cliente.endereco.cidade, cliente.endereco.numero, cliente.endereco.rua,  cliente.endereco.referencia,cliente.email))
        f.close()

    def puxar(self):
        list = []
        cliente = Cliente()
        f = open('cliente.txt', 'r')
        f.readline()
        while 1:
             cliente.nome = f.readline()
             cliente.telefone = f.readline()
             cliente.cpf = f.readline()
             cliente.endereco.cep = f.readline()
             cliente.endereco.cidade = f.readline()
             cliente.endereco.numero = f.readline()
             cliente.endereco.rua = f.readline()
             cliente.endereco.referencia = f.readline()
             cliente.email = f.readline()
             list.append(cliente)

             if not f.readline():
                 break

        f.close()
        return list