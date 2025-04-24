from aeronave import aeronave
from avioneta import avioneta
from helicoptero import helicoptero
from airbus360 import airbus360

# Crear un objeto en cada clase

obj_aeronave = aeronave()
obj_avioneta = avioneta()
obj_airbus360 = airbus360()
obj_helicoptero = helicoptero()

# Llamamos al método describir de cada objeto

obj_aeronave.describir()
obj_avioneta.describir()
obj_airbus360.describir()
obj_helicoptero.describir()


