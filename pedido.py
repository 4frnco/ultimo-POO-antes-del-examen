
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
