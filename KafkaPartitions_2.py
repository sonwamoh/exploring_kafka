import json
from kafka import KafkaProducer

# Pass key pair value to topics
# topic will decide partition on randomly based on key
# hash(record.key) % num_partitions = partition_number

topic_name = 'hello_world2'
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send(topic_name, key=b'foo', value=b'bar')
producer.send(topic_name, key=b'foo', value=b'bar')
producer.send(topic_name, key=b'foo', value=b'pub')
producer.send(topic_name, key=b'sue', value=b'club')

producer.close()
