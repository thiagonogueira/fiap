from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'py-producer', 
    bootstrap_servers='hdpdemo.local:6667', 
    group_id='my_favorite_group', 
    max_poll_interval_ms=1000, 
    heartbeat_interval_ms=200, 
    )
consumer.subscribe(topics=['py-producer'])

for msg in consumer:
    print(msg)
