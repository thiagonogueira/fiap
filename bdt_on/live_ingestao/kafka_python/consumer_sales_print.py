from kafka import KafkaConsumer

consumer = KafkaConsumer('MP_SALES', bootstrap_servers='hdpdemo.local:6667')
for msg in consumer:
    print(msg.value)
