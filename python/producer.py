from kafka import KafkaProducer
import json

TOPIC_NAME = "local-tkm-data"
bootstrap_servers=['localhost:9092', '172.104.185.225:9092']

payload = {
           "data_type":"BENEFICIALLY_OWNER",
           "data":[
              {
                 "bo_type":"b",
                 "lname":"last name BO 1",
                 "user_id":5118,
                 "created":"2021-06-15T15:19:54.814826",
                 "fname":"first name BO 1",
                 "id":62,
                 "nama_badan": None,
                 "modified":"2021-06-15T15:19:54.814834"
              },
              {
                 "bo_type":"b",
                 "lname":"last name BO 2",
                 "user_id":5117,
                 "created":"2021-06-15T12:11:28.673046",
                 "fname":"first name BO 2",
                 "id":61,
                 "nama_badan": None,
                 "modified":"2021-06-15T12:11:28.673054"
              }
           ],
           "timestamp":"2021-06-16T09:11:54.060674"
        }

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )

producer.send(TOPIC_NAME, value=payload)
producer.flush()
