from aeronave import aeronave

class avioneta(aeronave):
    def __init__(self, modelo, capacidad, tamaño, numeroMotores):
        super().__init__(modelo, capacidad, tamaño)
        self.numeroMotores = numeroMotores

    def describir(self):
        print ("Estoy respondiendo desde la clase avioneta")

    def backflipAire(self):
        pass

    def getNumeroMotores(self):
        pass

    def setNumeroMotores(self, value):
        pass