import requests
import json
from pyspark_output_produce import country_prize_category_topic, country_prize_gender_topic, year_category_laureates_topic

# {
#     "name": "postgres-json-data-sink6",
#     "config": {
#         "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
#         "connection.url": "jdbc:postgresql://localhost:5432/kafka_test",
#         "connection.user": "postgres",
#         "connection.password": "",
#         "topics": "mydata6",
#         "insert.mode": "insert",
#         "catalog.pattern": "nobel-postgres-sink6",
#         "value.converter": "org.apache.kafka.connect.json.JsonConverter",
#         "table.name.format": "kafka_connect.my_data_test4",
#         "auto.create": "true",
#         "auto.evolve": "true",
#         "value.converter.schemas.enable": "true",
#         "transforms": "flatten",
#         "transforms.flatten.type": "org.apache.kafka.connect.transforms.Flatten$Value",
#         "transforms.flatten.delimiter": "_"
#     }
# }

connector_url = 'http://127.0.0.1:8083/connectors'

topic_list = [country_prize_category_topic,
              country_prize_gender_topic, year_category_laureates_topic]

table_name_list = ['country_prize_category',
                   'country_prize_gender', 'year_category_laureates']

pk_fields_list = ['country', 'country', 'prize_year']


def create_sink(topic, name, table_name, pk_fields):
    sink_config = {
        "name": name,
        "config": {
            "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
            "connection.url": "jdbc:postgresql://localhost:5432/kafka_test",
            "connection.user": "postgres",
            "connection.password": "",
            "topics": topic,
            "insert.mode": "upsert",
            "catalog.pattern": name,
            "value.converter": "org.apache.kafka.connect.json.JsonConverter",
            "value.converter.schemas.enable": "true",
            "table.name.format": f"kafka_connect.{table_name}",
            "pk.mode": "record_value",
            "pk.fields": pk_fields,
            "auto.create": "true",
            "auto.evolve": "true"
        }
    }
    response = requests.post(connector_url, json=sink_config)
    return response


if __name__ == "__main__":
    i = 0
    for topic in topic_list:
        response = create_sink(
            topic, f"kafka-postgres-sink{i+1}", table_name_list[i], pk_fields_list[i])
        if response.status_code != 201:
            print(
                f"Could not create sink connector [kafka-postgres-sink{i+1}]. Error message is:")
            print(response.reason)
            break
        print(
            f"Sink connector [kafka-postgres-sink{i+1}] successfully created")
        print("======================================================")
        i += 1
    if i == 3:
        print("All sink connector creation successful")
