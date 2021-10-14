from confluent_kafka import Producer
import time
bootstrap_servers = 'hdpdemo.local:6667'

p = Producer({'bootstrap.servers': bootstrap_servers})
i = 0
while True:
   p.produce('py-producer', f'hello{i}')
   p.produce('py-producer', f'world{i}')
   i += 1
   time.sleep(0.5)
