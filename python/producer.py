from kafka import KafkaProducer
import json

TOPIC_NAME = "reaper-mpesa"
bootstrap_servers=['localhost:9092']

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )

producer.send(TOPIC_NAME, value={"hello": "producer"})
producer.flush()
