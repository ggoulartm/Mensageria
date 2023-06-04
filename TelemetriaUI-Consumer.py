from tkinter import *
import os

   

app = Tk()
app.title("TMR Veicular - Cliente")
app.geometry("600x200")

vehicleEvents = ["Velocidade do veiculo","RPM do motor","Temperatura do motor","Nivel de combustivel","Localizacao GPS","Status das luzes"]
Label(app,text="Evento:",background="#dde", foreground="#009",anchor=W).place(x=10,y=10,width=80,height=20)

lb_events=Listbox(app,height=6)

for element in vehicleEvents:
	lb_events.insert(END,element)

lb_events.pack()


for element in functions:
	lb_functions.insert(END, element)
	
lb_functions.pack()



app.mainloop()
