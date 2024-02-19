from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'Test_Topic_1',
    bootstrap_servers='localhost:9092',
    group_id='consume_group'
)

for message in consumer:
    print("Hey, Customers New Fruit Available")
    print(f'Received: {message.value.decode("utf-8")}')
