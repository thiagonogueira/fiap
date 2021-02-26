python
from confluent_kafka import Producer
import time
bootstrap_servers = 'localhost:9092'
p = Producer({'bootstrap.servers': bootstrap_servers})
for i in range(10000):
   p.produce('py-producer', f'hello{i}')
   p.produce('py-producer', f'world{i}')
   time.sleep(1)