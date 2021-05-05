import json
import time

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'MP_SALES', 
    bootstrap_servers='hdpdemo.local:6667', 
    group_id='fraud_detector', 
    max_poll_interval_ms=1000, 
    heartbeat_interval_ms=200, 
    )
consumer.subscribe(topics=['MP_SALES'])
for msg in consumer:
    time.sleep(1)
    if json.loads(msg.value)['after']['PRICE'] > 600:
        print(msg.value)
