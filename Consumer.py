import os
import subprocess
import pandas as pd
import json

def console_consumer_all(topic) -> None:
	consumidor=subprocess.Popen("kafka/bin/kafka-console-consumer.sh --topic "+topic+" --from-beginning --bootstrap-server localhost:9092 > output/output"+topic+".json")
	return consumidor.pid

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
 
def processJson(topic):
	with open('output'+topic+'.json') as user_file:
		file_content=user_file.read()
	arquivo=json.loads('['+file_content.strip().replace('}\n  ','},\n')+']')
	arquivo=json.dumps(arquivo,indent=2)
	return arquivo

def analyze(topic):
	df = pd.read_json(processJson(topic))
	return [df,df["Valor"].mean(),df["Valor"].max(),df["Valor"].min()]	


def exibicao(topic):
	analyze(topicToEvent(topic))[0].plot(x="Data-Hora",y="Valor", kind="bar",rot=20).savefig("/figs/"+topic+".png")
