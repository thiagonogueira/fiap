from kafka import KafkaConsumer

consumer = KafkaConsumer('primeiro', bootstrap_servers='hdpdemo.local:6667')
for msg in consumer:
    print(msg)
