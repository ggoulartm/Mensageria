from tkinter import *
from datetime import datetime
from Producer import *



def Publisher():
    datahora=datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    evento=str(lb_events.get(ACTIVE))
    valor=vValor.get()
    print("Evento: "+evento)
    print("Valor: "+valor)
    print("Horario: "+datahora)
    if evento == "Velocidade do veiculo":
        console_producer("velocidade",evento,valor,datahora)
    elif evento == "RPM do motor":
        console_producer("rpm",evento,valor,datahora)
    elif evento == "Temperatura do motor":
        console_producer("temperatura",evento,valor,datahora)
    elif evento == "Nivel de combustivel":
        console_producer("nivel-combustivel",evento,valor,datahora)
    elif evento == "Localizacao GPS":
        console_producer("GPS",evento,valor,datahora)
    else:
        console_producer("status-luzes",evento,valor,datahora)

def Sair():
    os.system("kafka/bin/kafka-server-stop.sh")
    os.system("kafka/bin/zookeeper-server-stop.sh")
    os.system("rm -rf /tmp/kafka-logs /tmp/zookeeper")
    app.destroy()

app = Tk()
app.title("TMR Veicular")
app.geometry("250x130")
app.resizable(0,0)

vehicleEvents = ["Velocidade do veiculo","RPM do motor","Temperatura do motor","Nivel de combustivel","Localizacao GPS","Status das luzes"]
Label(app,text="Evento:",background="#dde", foreground="#009",anchor=W).place(x=10,y=10,width=80,height=20)

framelb=Frame(app)
framelb.pack()


lb_events=Listbox(framelb,width=20,height=3, font=("Arial",10))
lb_events.pack(side="left",fill="y")

scrollbar=Scrollbar(framelb)
scrollbar.pack(side="right",fill="y")
scrollbar.config(command=lb_events.yview)

lb_events.config(yscrollcommand=scrollbar.set)

for element in vehicleEvents:
	lb_events.insert(END,element)

framelb.place(x=70,y=10)

Label(app,text="Valor:",background="#dde", foreground="#009",anchor=W).place(x=10,y=60,width=60,height=20)
vValor=Entry(app)
vValor.place(x=10,y=80,width=200,height=20)

publicar=Button(app,text="Publicar",command=Publisher)
publicar.place(x=45,y=105,width=55,height=20)

clear=Button(app,text="Limpar",command=clear_topics)
clear.place(x=105,y=105,width=55,height=20)

getout=Button(app,text="Sair",command=Sair)
getout.place(x=165,y=105,width=50,height=20)

[kafkaPID,zookeeperPID] = start_server()

app.mainloop()
