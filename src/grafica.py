from tkinter import DISABLED, Tk, Button, Label
from Bicicleta import Bicicleta
from dado import Dado

def turno():
    for i in range(5):
        miDado.lanzar()
        x = miDado.consultar()
        miDado.lanzar()
        y = miDado.consultar()
        partidor[i].irHasta(x, y)
        partidor[i].mostrar()
        d = partidor[i].distancia
        botones[i].place(x=10+d*10, y=250 - 50*i)
        if partidor[i].distancia >=90:
            bturno["state"]=DISABLED
            lMensaje["text"] = f"La ganadora es la bici {i}"
            break

ventanita = Tk()
ventanita.geometry("1000x400")
ventanita.title("Competencia de bicis")
partidor = [Bicicleta("") for x in range(5)]
botones = [Button() for x in range(5)]
miDado = Dado()
bturno = Button(text="Avanzar", command=turno)
bturno.place(x = 450, y = 350)
lMensaje = Label("")
lMensaje.place(x = 400, y = 300)
for i in range(5):
    partidor[i].propietario = str(i)
    botones[i]["text"] = str(i)
    botones[i].place(x=10, y=250 - 50*i)

ventanita.mainloop()