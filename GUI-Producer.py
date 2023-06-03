from tkinter import *
from datetime import datetime

def Publisher():
    datahora=datetime.now().strftime('%d/%m/%Y %H:%M')
    print("evento publicado"+str(lb_events.get(ACTIVE)+vValor.get()+datahora))
#acionar kafka

app = Tk()
app.title("Sistema de Telemetria Veicular")
app.geometry("400x200")

vehicleEvents = ["Velocidade do veiculo","RPM do motor","Temperatura do motor","Nivel de combustivel","Localizacao GPS","Status das luzes"]
Label(app,text="Evento:",background="#dde", foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)

lb_events=Listbox(app)

for element in vehicleEvents:
	lb_events.insert(END,element)

lb_events.pack()

Label(app,text="Valor",background="#dde", foreground="#009",anchor=W).place(x=10,y=100,width=100,height=20)
vValor=Entry(app)
vValor.place(x=10,y=120,width=200,height=20)

publicar=Button(app,text="Publicar",command=Publisher())
publicar.place(x=30,y=145,width=50,height=20)


app.mainloop()
