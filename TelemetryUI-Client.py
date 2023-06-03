from tkinter import *

class TelemetryClient:
	def __init__(self):
		self.window = Tk()
		self.window.title("Telemetria - Cliente")
		self.window.resizable(0,0)
		self.window.geometry("1280x720+300+200")
		
		self.frame1=Frame(self.window)
		self.frame1.pack()
		
		self.radio1=Radiobutton(self.frame1, text="analise", value = 0, command=None).pack(side="left")
		self.radio2=Radiobutton(self.frame1, text="exibicao", value = 1, command=None).pack(side="left")
		self.radio1=Radiobutton(self.frame1, text="armazenamento", value = 2, command=None).pack(side="right")
				
		self.window.mainloop()
		
TelemetryClient()
