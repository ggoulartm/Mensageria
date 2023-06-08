import os
import subprocess
import json

def start_server():
	from time import sleep
	zookeeper=subprocess.Popen(["kafka/bin/zookeeper-server-start.sh","kafka/config/zookeeper.properties"])
	kafka=subprocess.Popen(["kafka/bin/kafka-server-start.sh","kafka/config/server.properties"])
	create_topics()

	return [kafka.pid,zookeeper.pid]

def create_topics():
	if topicos_existentes("velocidade")==False:
		os.system("kafka/bin/kafka-topics.sh --create --topic velocidade --bootstrap-server localhost:9092")
	if topicos_existentes("rpm")==False:	
		os.system("kafka/bin/kafka-topics.sh --create --topic rpm --bootstrap-server localhost:9092")
	if topicos_existentes("temperatura")==False:
		os.system("kafka/bin/kafka-topics.sh --create --topic temperatura --bootstrap-server localhost:9092")
	if topicos_existentes("nivel-combustivel")==False:
		os.system("kafka/bin/kafka-topics.sh --create --topic nivel-combustivel --bootstrap-server localhost:9092")
	if topicos_existentes("quilometragem")==False:
		os.system("kafka/bin/kafka-topics.sh --create --topic quilometragem --bootstrap-server localhost:9092")
	if topicos_existentes("GPS")==False:
		os.system("kafka/bin/kafka-topics.sh --create --topic GPS --bootstrap-server localhost:9092")
	if (topicos_existentes("status-luzes"))==False:
		os.system("kafka/bin/kafka-topics.sh --create --topic status-luzes --bootstrap-server localhost:9092")

    
def clear_topics():
	os.system("kafka/bin/kafka-topics.sh --delete --topic velocidade --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --delete --topic rpm --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --delete --topic temperatura --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --delete --topic nivel-combustivel --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --delete --topic quilometragem --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --delete --topic GPS --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --delete --topic status-luzes --bootstrap-server localhost:9092")
	create_topics()

def console_producer(topic,event,value,time):
	post="kafka/bin/kafka-console-producer.sh --topic "+ str(topic) +" --bootstrap-server localhost:9092"
	mssg={
		"Evento":event,
		"Valor":float(value),
		"Data-Hora":time
	}
	mssg=json.dumps(mssg, indent=1)
	for chunk in json.JSONEncoder().iterencode(mssg):
		os.system('echo '+ chunk +' |'+post)
	
def topicos_existentes(topic):
	os.system("kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list > topicos.txt")
	with open('topicos.txt') as topicos:
		topics=topicos.read()
	existe=False
	for i in topics.split('\n'):
		if i==topic:
			existe=True
	return existe

