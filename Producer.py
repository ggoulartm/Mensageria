import os

def start_server():
	from time import sleep
	os.system("kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties &")
	os.system("kafka/bin/kafka-server-start.sh kafka/config/server.properties &")
	sleep(5)
	os.system("kafka/bin/kafka-topics.sh --create --topic velocidade --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --create --topic rpm --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --create --topic temperatura --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --create --topic nivel-combustivel --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --create --topic quilometragem --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --create --topic GPS --bootstrap-server localhost:9092")
	os.system("kafka/bin/kafka-topics.sh --create --topic status-luzes --bootstrap-server localhost:9092")

def console_producer(topic,value):
	os.system("echo "+str(value)+"| kafka/bin/kafka-console-producer.sh --topic "+topic+" --bootstrap-server localhost:9092")
	

