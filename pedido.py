
from data import Data
from cliente import Cliente
from produto import Produto

class Pedido:
    def __init__(self, cestaProdutos, cliente, data):
        self.cestaPedido = list()
