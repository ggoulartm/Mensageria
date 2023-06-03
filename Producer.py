"""from confluent_kafka import Producer, KafkaError  
  
if __name__ == '__main__':  
  
  topic = "<topic_stream_name>"  
  conf = {  
    'bootstrap.servers': "<bootstrap_servers_endpoint>", #usually of the form cell-1.streaming.<region>.oci.oraclecloud.com:9092  
    'security.protocol': 'SASL_SSL',  
  
    'ssl.ca.location': '</path/on/your/host/to/your/cert.pem/>',  # from step 6 of Prerequisites section
     # optionally instead of giving path as shown above, you can do 1. pip install certifi 2. import certifi and
     # 3. 'ssl.ca.location': certifi.where()
  
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '<OCI_tenancy_name>/<your_OCI_username>/<stream_pool_OCID>',  # from step 2 of Prerequisites section
    'sasl.password': '<your_OCI_user_auth_token>',  # from step 7 of Prerequisites section
   }  
  
   # Create Producer instance  
   producer = Producer(**conf)  
   delivered_records = 0  
  
   # Optional per-message on_delivery handler (triggered by poll() or flush())  
   # when a message has been successfully delivered or permanently failed delivery after retries.  
   def acked(err, msg):  
       global delivered_records  
       """Delivery report handler called on  
           successful or failed delivery of message """  
       if err is not None:  
           print("Failed to deliver message: {}".format(err))  
       else:  
           delivered_records += 1  
           print("Produced record to topic {} partition [{}] @ offset {}".format(msg.topic(), msg.partition(), msg.offset()))  

  for n in range(10):  
      record_key = "messageKey" + str(n)  
      record_value = "messageValue" + str(n)  
      print("Producing record: {}\t{}".format(record_key, record_value))  
      producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)  
      # p.poll() serves delivery reports (on_delivery) from previous produce() calls.  
      producer.poll(0)  

  producer.flush()  
  print("{} messages were produced to topic {}!".format(delivered_records, topic))
  """
  
def start_server():
	import os
	from time import sleep
	os.system("kafka_2.13-3.4.0/bin/zookeeper-server-start.sh config/zookeeper.properties &")
	os.system("kafka_2.13-3.4.0/bin/kafka-server-start.sh config/server.properties &")
	sleep 60
	os.system("kafka_2.13-3.4.0/bin/kafka-topics.sh --create --topic velocidade --bootstrap-server localhost:9092")
	os.system("kafka_2.13-3.4.0/bin/kafka-topics.sh --create --topic rpm --bootstrap-server localhost:9092")
	os.system("kafka_2.13-3.4.0/bin/kafka-topics.sh --create --topic temperatura --bootstrap-server localhost:9092")
	os.system("kafka_2.13-3.4.0/bin/kafka-topics.sh --create --topic nivel-combustivel --bootstrap-server localhost:9092")
	os.system("kafka_2.13-3.4.0/bin/kafka-topics.sh --create --topic quilometragem --bootstrap-server localhost:9092")
	os.system("kafka_2.13-3.4.0/bin/kafka-topics.sh --create --topic GPS --bootstrap-server localhost:9092")
	os.system("kafka_2.13-3.4.0/bin/kafka-topics.sh --create --topic status-luzes --bootstrap-server localhost:9092")

def console_producer(topic,value):
	os.system("echo "+str(value)+" kafka_2.13-3.4.0/bin/kafka-console-producer.sh --topic "+topic+" --bootstrap-server localhost:9092")
	

