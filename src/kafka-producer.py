import json

from confluent_kafka import Producer
from utils.config import load_config

config = load_config("./config.yaml")

kafka_broker = f'{config["kafka"]["host"]}:{config["kafka"]["port"]}'
kafka_topic = config["kafka"]["topic"]


p = Producer({"bootstrap.servers": kafka_broker})


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def delivery_report(err, msg):
    if err is not None:
        print("Message delivery failed: {}".format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))


some_data_source = [
    {"event": "user_signup", "user_id": 1, "timestamp": "2023-10-01T12:00:00Z"},
    {
        "event": "purchase",
        "user_id": 2,
        "amount": 29.99,
        "timestamp": "2023-10-01T12:05:00Z",
    },
    {"event": "user_login", "user_id": 3, "timestamp": "2023-10-01T12:10:00Z"},
    {
        "event": "item_view",
        "user_id": 1,
        "item_id": 101,
        "timestamp": "2023-10-01T12:15:00Z",
    },
    {"event": "user_logout", "user_id": 2, "timestamp": "2023-10-01T12:20:00Z"},
]


for data in some_data_source:
    p.poll(0)
    p.produce(kafka_topic, json_serializer(data), callback=delivery_report)

p.flush()
