def console_consumer(topic):
	os.system("/kafka/bin/kafka-console-consumer.sh --topic "+topic+" --from-beginning --bootstrap-server localhost:9092")


