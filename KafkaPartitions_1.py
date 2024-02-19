import json
from kafka import KafkaProducer

# Send events to specfic partitions

topic_name = 'hello_world1'
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))
data1 = {'number': 1}
data2 = {'number': 2}
data3 = {'number': 3}
data4 = {'number': 4}
data5 = {'number': 5}
data6 = {'number': 6}

producer.send(topic_name, value=data1, partition=1)
producer.send(topic_name, value=data2, partition=1)
producer.send(topic_name, value=data3, partition=1)
producer.send(topic_name, value=data4, partition=2)
producer.send(topic_name, value=data5, partition=2)
producer.send(topic_name, value=data6, partition=0)

producer.close()