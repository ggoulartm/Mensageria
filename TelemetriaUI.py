//UI Sistema de Mensageria com Kafka

From Tkinter import *


classe Application:
	def __init__(self,master=None):
		self.widget1 = Frame(master)
		self.widget1.pack()
		self.msg = Label(self.widget1, text = "Primeiro widget")
		self.msg.pack ()
		
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
		
		self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
		
        self.titulo = Label(self.primeiroContainer, text="Sistema de Telemetria Veicular")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Evento", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Valor", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
		
		self.publicar = Button(self.widget1)
		self.publicar["text"]="Publicar"
		self.publicar["font"]=("Calibri","10")
		self.publicar["width"]=5
		self.publicar["command"]=self.widget1.quit
		self.publicar.pack ()

root = Tk()
Application(root)
root.mainloop()
