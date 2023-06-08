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
  
		self.graph=PhotoImage(file="figs/velocidade.png")
		self.framegraph=Frame(self.app, bg="#3b3b3b").pack()
		self.label_graph=Label(self.framegraph, image=self.graph)
		self.label_graph.pack()
		
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
  
		#self.Importar=Button(self.app,text="Atualizar",command=self.getPlot)
		#self.Importar.place(x=10,y=330,width=50,height=20)
		
  		#media,max,min
		#analyze(self.lb_events.get(ACTIVE))
		
		self.label_max=Label(self.app,text="Máximo:")
		self.label_avg=Label(self.app,text="Médio:")
		self.label_min=Label(self.app,text="Mínimo:")
  
		self.label_max.place(x=300,y=330)
		self.label_avg.place(x=300,y=350)
		self.label_min.place(x=300,y=370)

		self.app.after(1000,self.updateLabel)
		self.app.after(1000,self.getPlot)
		self.app.mainloop()
  
	def getPlot(self):
		#plotagens
		listen_all()
		exibicao(self.lb_events.get(ACTIVE))
		self.graph=PhotoImage(file="figs/velocidade.png")
		self.label_graph.configure(image=self.graph)
		self.app.after(10000,self.getPlot)
  
	def updateLabel(self):
		self.label_max.configure(text="Máximo:"+str(analyze("velocidade")[2]))
		self.label_avg.configure(text="Médio:"+str(analyze("velocidade")[1]))
		self.label_min.configure(text="Mínimo:"+str(analyze("velocidade")[3]))
		self.app.after(10000,self.updateLabel)

  
TelemetryClient()
