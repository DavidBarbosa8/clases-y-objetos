# -*- coding: utf-8 -*-
from aeronave import aeronave;

class helicoptero(aeronave):
    def __init__(self, modelo, capacidad, tamaño, numeroHelices):
        super().__init__(modelo, capacidad, tamaño)
        self.numeroHelices = numeroHelices

    def volar(self):
        pass

    def describir(self):
        print ("Estoy respondiendo desde la clase helicoptero")

    def despegarVerticalmente(self):
        pass

    def getNumeroHelices(self):
        pass

    def setNumeroHelices(self, value):
        pass