from confluent_kafka import Consumer, KafkaException, KafkaError
import time

conf = {
    "bootstrap.servers": "boot-zlqiji0t.c3.kafka-serverless.us-east-1.amazonaws.com 9098",
    "group.id": "python-consumer-group",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(conf)
consumer.subscribe(["new_topic"])

start_time = time.time()

timeout_duration = 10

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"Fin de la particion {msg.partition} en {msg.topic}")
            else:
                raise KafkaException(msg.error())
        else:
            print(f"mensaje recibido: {msg.value().decode('utf-8')} de {msg.topic()}")
finally:
    consumer.close()