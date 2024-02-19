import json
from kafka import KafkaProducer

# There are two event key types ping & pong
#checking out how partition no. is computed by partitioner

topic_name = 'hello_world3'
producer = KafkaProducer(bootstrap_servers='localhost:9092', key_serializer=str.encode,
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))
data1 = {'number': 1}
data2 = {'number': 2}
data3 = {'number': 3}
data4 = {'number': 4}
data5 = {'number': 5}
data6 = {'number': 6}

producer.send(topic_name, key='ping', value='data1')
producer.send(topic_name, key='pong', value='data2')
producer.send(topic_name, key='pong', value='data3')
producer.send(topic_name, key='ping', value='data4')

producer.close()
