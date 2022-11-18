import json
from kafka import KafkaConsumer

from api_fetch_produce import bootstrap_server, topic


def json_deserializer(data):
    return json.loads(data.decode('utf-8'))


def consume():
    consumer = KafkaConsumer(
        topic, bootstrap_servers=bootstrap_server, auto_offset_reset='earliest', value_deserializer=json_deserializer)
    # )
    # write the message to a json file
    # there is only one message in the topic
    msg_count = 0
    for msg in consumer:
        msg_count += 1
        with open('data/laureates_data.json', 'w') as f:
            json.dump(msg.value, f)
        print("written msg, to laureates_data.json".format(msg_count))
        print(msg.value)
        break


if __name__ == "__main__":
    consume()
