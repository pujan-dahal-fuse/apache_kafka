# **Apache Kafka Installation and Commands**

Apache Kafka is maintained by confluent. To get a confluent version of Apache Kafka, sign up to [confluent](https://www.confluent.io/get-started/), and download the confluent-kafka zip file and unzip it. Move the unzipped folder to project folder. Add the `<confluent_folder_path>/bin/` to path variable in your operating system, so that you can access kafka commands easily.

Since, I'm using fish_shell, I use:

`fish_add_path <confluent_folder_path>/bin/`

Commands to run kafka and to write/read message to/from topics:

1.  Start the zookeeper server:  
    `zookeeper-server-start <path_to_confluent_folder>/etc/kafka/zookeeper.properties`
2.  In another terminal, start the kafka server:  
    `kafka-server-start <path_to_confluent_folder>/etc/kafka/server.properties`
3.  In another terminal, create/list the topics:
    1.  To list the topics:  
        `kafka-topics --bootstrap-server localhost:9092 --list`
    2.  To create a topic:  
        `kafka-topics --bootstrap-server localhost:9092 --create --topic <topic_name>`
    3.  To delete topic:  
        `kafka-topics --bootstrap-server localhost:9092 --delete --topic <topic_name>`
    4.  Describe topic:  
        `kafka-topics --bootstrap-server localhost:9092 --describe --topic <topic_name>`
    5.  Create topic with different number of partitions:  
        `kafka-topics --bootstrap-server localhost:9092 --create --topic <topic_name> – partitions <num_partitions>`
    6.  To specify a replication factor, add following to above command:  
        `--replication-factor <num_of_replicas>`
    7.  To alter the number of partitions in already created topic:  
        `kafka-topics --bootstrap-server localhost:9092 --alter --topic <topic_name> --partitions <num_partitions>`
4.  Write some events into the topic:
    1.  Create a producer by specifying the topic:  
        `kafka-console-producer --bootstrap-server localhost:9092 --topic <topic_name>`
    2.  Write message in the console
5.  Read events from the topic:
    1.  Create a consumer by specifying the topic:  
        `kafka-console-consumer --bootstrap-server localhost:9092 --topic <topic_name>`
    2.  Additionally, provide `--from-beginning` to read message from beginning; however, this doesn't guarantee the ordering of messages
    3.  Further, to specify a consumer group for the consumer process, include:  
        `--group <group_name>`
6.  Managing consumer groups:
    1.  List all consumer groups:  
        `kafka-consumer-groups --bootstrap-server localhost:9092 --list`
    2.  Describe a consumer group:  
        `kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group <group_name>`
    3.  Deleting a consumer group:  
        `kafka-consumer-groups --bootstrap-server localhost:9092 --delete --group <group_name>`

Notes: A consumer group is a group of consumers, which can read in a combined manner. Data/message read by one consumer is not read by another consumer within a consumer group. We know that a topic is divided into multiple partitions: each consumer in a consumer group is assigned partition/s to read from:

1.  It there are 4 partitions and 1 consumer, the consumer can read from all partitions.
2.  If there are 4 partitions and 2 consumers, then 1 consumer can read from 2 partitions, another from another 2 partitions.
3.  If there are 4 partitions and 3 consumers, 2 consumers can read from 1 partition each and 1 consumer can read from 2 partitions.
4.  If there are 4 partitions and 4 consumers, each consumer can read from 1 partitions.
5.  If there are 4 partitions and 5 consumers, 4 consumers can read from one partitions each and 1 consumer cannot read at all; it remains idle.

\_\_consumer_offset is recorded in a topic in kafka, which gives the offset within a partition that a consumer was reading from. In case the consumer fails and then restarts, the consumer knows where to read from using the offset.
