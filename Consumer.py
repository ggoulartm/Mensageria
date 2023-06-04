import os
import pandas as pd

def console_consumer_all(topic):
	os.system("/kafka/bin/kafka-console-consumer.sh --topic "+topic+" --from-beginning --bootstrap-server localhost:9092 >> output"+topic+".json &")

def console_consumer(topic):
	os.system("/kafka/bin/kafka-console-consumer.sh --topic "+topic+" --bootstrap-server localhost:9092")

def listen(evento):
    #evento=str(lb_events.get(ACTIVE))
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
    	
def importJson():
	console_consumer_all("velocidade")
    	console_consumer_all("rpm")
    	console_consumer_all("temperatura")
    	console_consumer_all("nivel-combustivel")
    	console_consumer_all("GPS")
    	console_consumer_all("status-luzes")
    	
def jsonToCsv(topic):
	df = pd.read_json("output"+topic+".json")
	df.to_csv()

	
