
class Produto:
    def __init__(self, nome, prezo, cantidadeStock):
        self.nome = nome
        self.setPrezo(prezo)
        self.setCantidadeStock(cantidadeStock)

    def setNome (self, nome):
        self.__nome = abs(nome)

    def getNome (self):
        return self.__nome

    def setPrezo(self, prezo):
        self.__prezo = abs(prezo)

    def getPrezo(self):
        return self.__prezo

    def setCantidadeStock (self, cantidadeStock):
        self.__cantidadeStock = abs(cantidadeStock)

    def getCantidadeStock(self):
        return self.__cantidadeStock

    def decrementarStock (self, cantidade):
        if self.__cantidadeStock > cantidade:
            self.__cantidadeStock -= cantidade
            return True
        else:
            return False

    def incrementarStock (self, cantidade):
        if self.__cantidadeStock < cantidade:
            self.__cantidadeStock += cantidade
            return True
        else:
            return False

    nome = property (getNome,setNome)
    prezo = property (getPrezo,setPrezo)
    cantidadStock = property (getCantidadeStock,setCantidadeStock)


