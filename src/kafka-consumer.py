from confluent_kafka import Consumer
from utils.config import load_config

config = load_config("./config.yaml")

kafka_broker = f'{config["kafka"]["host"]}:{config["kafka"]["port"]}'
kafka_topic = config["kafka"]["topic"]
kafka_group_id = config["kafka"]["group-id"]
kafka_offset_reset = config["kafka"]["auto-offset-reset"]

c = Consumer(
    {
        "bootstrap.servers": kafka_broker,
        "group.id": kafka_group_id,
        "auto.offset.reset": kafka_offset_reset,
        "enable.auto.commit": True,
    }
)

c.subscribe([kafka_topic])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print("Received message: {}".format(msg.value().decode("utf-8")))
