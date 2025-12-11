
from data import Data
from cliente import Cliente
from produto import Produto

class Pedido:
    def __init__(self, cestaProdutos, cliente, data):
        self.cestaPedido = list() #[]
        self.cliente = cliente
        self.data = data

    def getCestaPedido (self):
        return self.cestaPedido

    def getCliente (self):
        return self.cliente

    def getData (self):
        return self.data

    def engadirProduto (self, produto, cantidade):
        if produto.decrementarStock(cantidade):
            self.cestaPedido.append ((produto, cantidade))

    def calculoPrezoTotal (self):
        total = 0
        for entrada in self.cestaPedido:
            total = total + entrada[1] * entrada[0].getPrezo()
        return total

p = Pedido (Cliente ('Manuel', 'm@gmail.com', 'aqui','36201')(Data(23, 3, 2025)))

peras = Produto('Peras', '2', '100')
manzana = Produto('Manzana', '1.50', '100')

p.engadirProduto(peras,2)
p.engadirProduto(manzana, 2)
print (p.calculoPrezoTotal())



