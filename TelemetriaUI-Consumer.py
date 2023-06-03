from tkinter import *
from datetime import datetime
from Consumer import *
import os

def console_consumer(topic):
	os.subprocess.check_output("/kafka/bin/kafka-console-consumer.sh --topic "+topic+" --from-beginning --bootstrap-server localhost:9092")

def listen():
    evento=str(lb_events.get(ACTIVE))
    if evento == "Velocidade do veiculo":
    	console_consumer("velocidade")
    elif evento == "RPM do motor":
    	console_consumer("rpm")
    elif evento == "Temperatura do motor":
    	console_consumer("temperatura")
    elif evento == "Nivel de combustivel":
    	console_consumer("nivel-combustivel")
    elif evento == "Localizacao GPS":
    	console_consumer("GPS")
    else:
    	console_consumer("status-luzes")
    

app = Tk()
app.title("TMR Veicular - Cliente")
app.geometry("600x200")

vehicleEvents = ["Velocidade do veiculo","RPM do motor","Temperatura do motor","Nivel de combustivel","Localizacao GPS","Status das luzes"]
Label(app,text="Evento:",background="#dde", foreground="#009",anchor=W).place(x=10,y=10,width=80,height=20)

lb_events=Listbox(app,height=6)

for element in vehicleEvents:
	lb_events.insert(END,element)

lb_events.pack()




app.mainloop()
