from tkinter import *
from datetime import datetime

def Publisher():
    datahora=datetime.now().strftime('%d/%m/%Y %H:%M')
    print("Evento: "+str(lb_events.get(ACTIVE)))
    print("Valor: "+vValor.get())
    print("Horario: "+datahora)
#acionar kafka

app = Tk()
app.title("TMR Veicular")
app.geometry("250x170")
app.maxsize(250,170)
app.minsize(250,170)

vehicleEvents = ["Velocidade do veiculo","RPM do motor","Temperatura do motor","Nivel de combustivel","Localizacao GPS","Status das luzes"]
Label(app,text="Evento:",background="#dde", foreground="#009",anchor=W).place(x=10,y=10,width=80,height=20)

lb_events=Listbox(app,height=6)

for element in vehicleEvents:
	lb_events.insert(END,element)

lb_events.pack()

Label(app,text="Valor",background="#dde", foreground="#009",anchor=W).place(x=10,y=100,width=60,height=20)
vValor=Entry(app)
vValor.place(x=10,y=120,width=200,height=20)

publicar=Button(app,text="Publicar",command=Publisher)
publicar.place(x=100,y=145,width=50,height=20)


app.mainloop()