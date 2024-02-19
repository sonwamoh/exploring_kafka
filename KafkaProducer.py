from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import random
import time

# Generate Fruit data-set
fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Watermelon']
cities = ['Chennai', 'Mumbai', 'Delhi', 'Kolkata', 'Bangalore']

num_entries = random.randint(5, 10)
dataset = []

for _ in range(num_entries):
    entry = {
        'productname': random.choice(fruits),
        'price': round(random.uniform(20, 50), 2),
        'city': random.choice(cities)
    }
    dataset.append(entry)

fruit_data = dataset

# Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))

current_retry, max_retries = 0, 3

topic = 'Test_Topic_1'

while current_retry < max_retries:
    try:
        for fruit in fruit_data:
            producer.send(topic, value=fruit)
            print(f'Fruits recently added: {fruit} ')
        break

    except NoBrokersAvailable as e:
        print(f"Error: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)
        current_retry += 1


producer.close()
