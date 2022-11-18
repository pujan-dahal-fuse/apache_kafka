import requests
import json
from kafka import KafkaProducer

bootstrap_server = ['localhost:9092']
topic = 'laureates'
nobel_laureates_url = "http://api.nobelprize.org/v1/laureate.json?gender=All"
headers = {"accept": "application/json"}


def jprint(obj):
    """
    create formatted string of python JSON object
    """
    text = json.dumps(obj, sort_keys=False, indent=4)
    print(text)


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


def produce(producer, topic, data):
    producer.send(topic, data)
    producer.flush()


def produce_message():
    response = requests.get(nobel_laureates_url, headers=headers)
    if response.status_code != 200:
        print(
            f"Error in reading data from url\nError: {response.status_code}, Message: {response.reason}")
        return
    try:
        producer = KafkaProducer(bootstrap_servers=bootstrap_server,
                                 value_serializer=json_serializer)
    except:
        print("Error! Could not create kafka producer")
        return
    # because json data is nested inside "laureates" key we create an array that contains all values inside laureates key
    produce(producer, topic, response.json())
    print("Successfully produced to topic {} message:".format(
        topic))
    jprint(response.json())


if __name__ == '__main__':
    produce_message()
