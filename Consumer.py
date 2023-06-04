import os
import pandas as pd

def console_consumer_all(topic) -> None:
	os.system("kafka/bin/kafka-console-consumer.sh --topic "+topic+" --from-beginning --bootstrap-server localhost:9092 >> output/output"+topic+".json &")

def listen_all():
	console_consumer_all("velocidade")
	console_consumer_all("rpm")
	console_consumer_all("temperatura")
	console_consumer_all("nivel-combustivel")
	console_consumer_all("GPS")
	console_consumer_all("status-luzes")

def console_consumer(topic):
	os.system("kafka/bin/kafka-console-consumer.sh --topic "+topic+" --bootstrap-server localhost:9092")

def topicToEvent(topic):
	if topic == "Velocidade do veiculo":
		event="velocidade"
	elif topic == "RPM do motor":
		event="rpm"
	elif topic == "Temperatura do motor":
		event="temperatura"
	elif topic == "Nivel de combustivel":
		event="nivel-combustivel"
	elif topic == "Localizacao GPS":
		event="GPS"
	else:
		event="status-luzes"
	return event

def listen(evento):
    #evento=str(lb_events.get(ACTIVE))
    console_consumer(topicToEvent(evento))

    	
def importJson():
	console_consumer_all("velocidade")
	console_consumer_all("rpm")
	console_consumer_all("temperatura")
	console_consumer_all("nivel-combustivel")
	console_consumer_all("GPS")
	console_consumer_all("status-luzes")
    	
def analyze(topic):
	df = pd.read_json("output/output"+topic+".json")
	return [df,df["Valor"].mean(),df["Valor"].max(),df["Valor"].min()]	


def exibicao(topic):
	analyze(topicToEvent(topic))[0].plot(x="Data-Hora",y="Valor", kind="bar",rot=20).savefig("/figs/"+topic+".png")
