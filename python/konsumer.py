from kafka import KafkaConsumer
import json

TOPIC_NAME = "local-tkm-data"
bootstrap_servers=['localhost:9092', '172.104.185.225:9092']
group_id = "local-tkm-group"


consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

for m in consumer:
    print(m.value)
