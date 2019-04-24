class Lampada:
    def __init__(self, tipo, voltagem, cor, marca, preco, potencia, status):
        self.tipo = tipo
        self.voltagem = voltagem
        self.cor = cor
        self.marca = marca
        self.preco = preco
        self.potencia = potencia
        self.status = status

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getVoltagem(self):
        return self.voltagem
    
    def setVoltagem(self, v):
        self.voltagem = v
    
    def getCor(self):
        return self.cor
    
    def setCor(self, cor):
        self.cor = cor
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getPreco(self):
        return self.preco
    
    def setPreco(self, preco):
        self.preco = preco

    def getPotencia(self):
        return self.potencia
    
    def setPotencia(self, potencia):
        self.potencia = potencia

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
    


    def getLampada(self):
        return "Lampada: {0} \nVoltagem: {1}\nCor: {2}\nMarca: {3}\nPreço: {4}\nPotencia: {5}\nStatus: {6}".format(self.getTipo(), self.getVoltagem(), self.getCor(), self.getMarca(), self.getPreco(), self.getPotencia(), self.getStatus())
        #str("Lampada: ", self.getTipo(), " Voltagem: ", self.getVoltagem(), " Cor: ", self.getCor(), " Marca: ", self.getMarca(), "Preço: ", self.getPreco(), " Potencia: ", self.getPotencia(), " Status: ", self.getStatus())

