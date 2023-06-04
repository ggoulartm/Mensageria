from tkinter import *

class TelemetryClient:
	def __init__(self):
		self.app = Tk()
		self.app.title("Telemetria - Cliente")
		self.app.resizable(0,0)
		self.app.geometry("900x600+300+200")
		
		self.vehicleEvents = ["Velocidade do veiculo","RPM do motor","Temperatura do motor","Nivel de combustivel","Localizacao GPS","Status das luzes"]
				
		self.frame1=Frame(self.app)
		self.frame1.pack()
		
		self.radio1=Radiobutton(self.frame1, text="analise", value = 0, command=None).pack(side="left")
		self.radio2=Radiobutton(self.frame1, text="exibicao", value = 1, command=None).pack(side="left")
		self.radio3=Radiobutton(self.frame1, text="armazenamento", value = 2, command=None).pack(side="right")
		
		
		self.framelb=Frame(self.app)
		self.framelb.pack()


		self.lb_events=Listbox(self.framelb,width=20,height=2, font=("Arial",10))
		self.lb_events.pack(side="left",fill="y")

		self.scrollbar=Scrollbar(self.framelb)
		self.scrollbar.pack(side="right",fill="y")
		self.scrollbar.config(command=self.lb_events.yview)

		self.lb_events.config(yscrollcommand=self.scrollbar.set)

		for element in self.vehicleEvents:
			self.lb_events.insert(END,element)

		self.framelb.place(x=70,y=10)
		
		
		self.app.mainloop()
		
TelemetryClient()
