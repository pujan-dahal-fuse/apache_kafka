import requests
import json
from pyspark_output_produce import topic_list

connector_url = 'http://127.0.0.1:8083/connectors'

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
    sink_creation_success = True
    for i in range(len(topic_list)):
        response = create_sink(
            topic_list[i], f"kafka-postgres-sink{i+1}", table_name_list[i], pk_fields_list[i])
        if response.status_code != 201:
            print(
                f"Could not create sink connector [kafka-postgres-sink{i+1}]. Error message is:")
            print(response.reason)
            sink_creation_success = False
            break
        print(
            f"Sink connector [kafka-postgres-sink{i+1}] successfully created")
        print("======================================================")

    if sink_creation_success:
        print("All sink connector creation successful")
