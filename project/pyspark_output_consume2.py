import json
from kafka import KafkaConsumer

from pyspark_output_consume1 import json_deserializer, consume
from pyspark_output_produce import bootstrap_server, country_prize_gender_topic


if __name__ == "__main__":
    consume(country_prize_gender_topic)
