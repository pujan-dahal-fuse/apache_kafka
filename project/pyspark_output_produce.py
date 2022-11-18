import json
from kafka import KafkaProducer
from api_fetch_produce import jprint
from schemas import country_prize_category_schema, country_prize_gender_schema, year_category_laureates_schema

bootstrap_server = ['localhost:9092']

country_prize_category_topic = 'topic1'
country_prize_gender_topic = 'topic2'
year_category_laureates_topic = 'topic3'

# create topic list, schema list to iterate through it
topic_list = [country_prize_category_topic,
              country_prize_gender_topic, year_category_laureates_topic]
schema_list = [country_prize_category_schema,
               country_prize_gender_schema, year_category_laureates_schema]

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

    producer_list = []
    try:
        for i in range(len(topic_list)):
            producer = KafkaProducer(bootstrap_servers=bootstrap_server,
                                     value_serializer=json_serializer)
            producer_list.append(producer)
    except:
        print("Error! Could not create kafka producer")
        return

    # the production of all data should be done sequentially (data to one topic should be completed before sending data to another topic)

    # json data list to iterate through it
    json_data_list = [country_prize_category_json_data,
                      country_prize_gender_json_data, year_category_laureates_json_data]

    if len(topic_list) != len(json_data_list) or len(topic_list) != len(schema_list):
        print("You have not specified topic_list, json_data_list, schema_list properly")
        return

    for i in range(len(topic_list)):
        for item in json_data_list[i]:
            data_to_send = {
                "schema": schema_list[i],
                "payload": item
            }
            produce(producer_list[i], topic_list[i], data_to_send)
        print(
            f'Finished producing data by Producer{i+1}.\n===============================================')

    print('All data production tasks completed...Exiting...')


if __name__ == '__main__':
    produce_message()
