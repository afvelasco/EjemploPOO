from dado import Dado
from Bicicleta import Bicicleta
from math import sqrt

partidor = [Bicicleta("") for x in range(10)]
miDado = Dado()
hayGanador = False
while (not hayGanador):
    for i in range(10):
        partidor[i].propietario = str(i)
        miDado.lanzar()
        x = miDado.consultar()
        miDado.lanzar()
        y = miDado.consultar()
        partidor[i].irHasta(x, y)
        partidor[i].mostrar()
        if partidor[i].distancia >=10:
            hayGanador = True
            break
print(f"El ganador es {i}")


