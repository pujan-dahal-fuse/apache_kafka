import json
from kafka import KafkaConsumer

from pyspark_output_produce import bootstrap_server, country_prize_category_topic


def json_deserializer(data):
    return json.loads(data.decode('utf-8'))


def consume(topic):
    consumer = KafkaConsumer(
        topic, bootstrap_servers=bootstrap_server, auto_offset_reset='earliest', value_deserializer=json_deserializer)
    msg_count = 0
    for msg in consumer:
        msg_count += 1
        print(
            f"Read message number {msg_count} from topic {topic}. Message is:")
        print(msg.value)
        print("===============================================")


if __name__ == "__main__":
    consume(country_prize_category_topic)
