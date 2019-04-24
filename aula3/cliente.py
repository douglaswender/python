class Cliente:

    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
    
    def getCliente(self):
        return 'Nome: {0} \nIdade: {1} \nCidade: {2}'.format(self.nome, self.idade, self.cidade)

    def getNome(self):
        return 'Nome: %s' % self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return ("Idade: %s" % self.idade)
    
    def setIdade(self, idade):
        self.idade = idade
        
    def getCidade(self):
        return ("Cidade: %s" % self.cidade)

    def setCidade(self, cidade):
        self.cidade = cidade

    
