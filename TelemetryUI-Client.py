from tkinter import *
from Consumer import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

listen_all() #melhorar a situação do consumer para não duplicar as mensagens
class TelemetryClient:
	def __init__(self):
		self.app = Tk()
		self.app.title("Telemetria - Cliente")
		self.app.resizable(0,0)
		self.app.geometry("500x400+300+200")
		
  		#menu de eventos
		self.vehicleEvents = ["Velocidade do veiculo","RPM do motor","Temperatura do motor","Nivel de combustivel","Localizacao GPS","Status das luzes"]
		self.framelb=Frame(self.app)
		self.framelb.pack()
		self.lb_events=Listbox(self.framelb,width=20,height=3, font=("Arial",10))
		self.lb_events.pack(side="left",fill="y")
		self.scrollbar=Scrollbar(self.framelb)
		self.scrollbar.pack(side="right",fill="y")
		self.scrollbar.config(command=self.lb_events.yview)
		self.lb_events.config(yscrollcommand=self.scrollbar.set)
		for element in self.vehicleEvents:
			self.lb_events.insert(END,element)
		self.framelb.place(x=100,y=330)
		
		self.graph=PhotoImage(file="figs/velocidade.png")
		self.framegraph=Frame(self.app, bg="#3b3b3b").pack()
		self.label_graph=Label(self.framegraph, image=self.graph).pack()
  
		self.Importar=Button(self.app,text="getPlot",command=self.getPlot)
		self.Importar.place(x=10,y=330,width=50,height=20)
		
  		#media,max,min
		#analyze(self.lb_events.get(ACTIVE))
		
		self.label_max=Label(self.app,text="Máximo:"+str(analyze("velocidade")[2])).place(x=300,y=330)
		self.label_avg=Label(self.app,text="Médio:"+str(analyze("velocidade")[1])).place(x=300,y=350)
		self.label_min=Label(self.app,text="Mínimo:"+str(analyze("velocidade")[3])).place(x=300,y=370)
  
		self.app.mainloop()
	def getPlot(self):
		#plotagens
		exibicao(self.lb_events.get(ACTIVE))
  
TelemetryClient()
