import json
from kafka import KafkaProducer
from api_fetch_produce import jprint
from schemas import country_prize_category_schema, country_prize_gender_schema, year_category_laureates_schema

bootstrap_server = ['localhost:9092']
# country_prize_category_topic = 'country_prize_category'
# country_prize_gender_topic = 'country_prize_gender'
# year_category_laureates_topic = 'year_category_laureates'

country_prize_category_topic = 'topic1'
country_prize_gender_topic = 'topic2'
year_category_laureates_topic = 'topic3'

country_prize_category_file = './data/country_prize_category.json'
country_prize_gender_file = './data/country_prize_gender.json'
year_category_laureates_file = './data/year_category_laureates.json'


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
    # open file for reading data
    with open(country_prize_category_file, 'r') as f1:
        country_prize_category_json_data = json.load(f1)

    with open(country_prize_gender_file, 'r') as f2:
        country_prize_gender_json_data = json.load(f2)

    with open(year_category_laureates_file, 'r') as f3:
        year_category_laureates_json_data = json.load(f3)
    try:
        producer1 = KafkaProducer(bootstrap_servers=bootstrap_server,
                                  value_serializer=json_serializer)
        producer2 = KafkaProducer(bootstrap_servers=bootstrap_server,
                                  value_serializer=json_serializer)
        producer3 = KafkaProducer(bootstrap_servers=bootstrap_server,
                                  value_serializer=json_serializer)
    except:
        print("Error! Could not create kafka producer")
        return

    # the production of all data should be done sequentially (data to one topic should be completed before sending data to another topic)
    for item in country_prize_category_json_data:
        data_to_send = {
            "schema": country_prize_category_schema,
            "payload": item
        }
        produce(producer1, country_prize_category_topic, data_to_send)
    print('Finished producing country_prize_category_data by Producer1.\n===============================================')

    for item in country_prize_gender_json_data:
        data_to_send = {
            "schema": country_prize_gender_schema,
            "payload": item
        }
        produce(producer2, country_prize_gender_topic, data_to_send)
    print('Finished producing country_prize_gender_data by Producer2.\n===============================================')

    for item in year_category_laureates_json_data:
        data_to_send = {
            "schema": year_category_laureates_schema,
            "payload": item
        }
        produce(producer3, year_category_laureates_topic, data_to_send)
    print('Finished producing year_category_laureates_data by Producer3.\n===============================================')

    print('All data production tasks completed...Exiting...')


if __name__ == '__main__':
    produce_message()
