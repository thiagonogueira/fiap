from kafka import KafkaConsumer

consumer = KafkaConsumer('primeiro', bootstrap_servers='hdpdemo.local:6667', group_id='my_favorite_group')
for msg in consumer:
    print(msg)
