from aeronave import aeronave

class airbus360(aeronave):
    def __init__(self, modelo, capacidad, tamaño, cantidadPasajeros):
        super().__init__(modelo, capacidad, tamaño)
        self.cantidadPasajeros = cantidadPasajeros

    def describir(self):
        print ("Estoy en un Airbus 360")

    def pilotoAutomatico(self):
        pass

    def getCantidadPasajeros(self):
        pass

    def setCantidadPasajeros(self, value):
        pass
    



