from kafka import KafkaConsumer
import json

TOPIC_NAME = "reaper-mpesa"

consumer = KafkaConsumer(
    TOPIC_NAME,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

for m in consumer:
    print(m.value)
