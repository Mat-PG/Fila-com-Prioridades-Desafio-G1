class Paciente:

    def __init__(self):
        self.nome = ""
        self.tipoSanguineo = 0
        self.dataNascimento = ""

    def setNome(self, nome):
        self.nome = nome
    
    def settipoSanguineo(self, sangue):
        self.tipoSanguineo = sangue
    
    def setdataNascimento(self, nascimento):
        self.dataNascimento = nascimento
    
    def getNome(self):
        return self.nome
    
    def gettipoSanguineo(self):
        return self.tipoSanguineo

    def getdataNascimento(self):
        return self.dataNascimento
  
