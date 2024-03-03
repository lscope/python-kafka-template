from kafka import (
    KafkaProducer,
    KafkaConsumer,
)
from kafka.errors import NoBrokersAvailable
import time
from pykafka.config import (
    KAFKA_PORT,
    KAFKA_HOST,
    KAFKA_TOPIC,
)




def get_kafka_producer(
        host: str=KAFKA_HOST,
        port: int=KAFKA_PORT,
    ) -> KafkaProducer:
    """
    Get a Kafka producer instance.

    Args:
        host (str): The Kafka server host. Defaults to KAFKA_HOST.
        port (int): The Kafka server port. Defaults to KAFKA_PORT.

    Returns:
        KafkaProducer: The Kafka producer instance.

    Raises:
        NoBrokersAvailable: If unable to connect to Kafka server after 10 attempts.
    """
    for i in range(10):
        try:
            producer = KafkaProducer(
                bootstrap_servers=f"{host}:{port}",
                value_serializer=lambda v: v.encode("utf-8")
            )
            break
        except NoBrokersAvailable:
                print(f"Attempt {i+1} to connect to Kafka server failed. Sleep 5 seconds and try again.")
                time.sleep(5)
    else:
        print("Could not connect to Kafka server after 10 attempts")
        exit(1)

    return producer


def get_kafka_consumer(
        topic: str=KAFKA_TOPIC,
        host: str=KAFKA_HOST,
        port: int=KAFKA_PORT,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="my-group",
    ) -> KafkaConsumer:
    """
    Get a Kafka consumer instance.

    Args:
        topic (str, optional): The Kafka topic to consume from. Defaults to KAFKA_TOPIC.
        host (str, optional): The Kafka host. Defaults to KAFKA_HOST.
        port (int, optional): The Kafka port. Defaults to KAFKA_PORT.
        auto_offset_reset (str, optional): The strategy to reset the offset when there is no initial offset in Kafka or if the current offset does not exist any more on the server. Defaults to "earliest".
        enable_auto_commit (bool, optional): Whether to enable auto commit of consumed offsets. Defaults to True.
        group_id (str, optional): The consumer group id. Defaults to "my-group".

    Returns:
        KafkaConsumer: The Kafka consumer instance.

    Raises:
        NoBrokersAvailable: If no Kafka brokers are available after 10 attempts.
    """
    for i in range(10):
        try:
            consumer = KafkaConsumer(
                topic,
                bootstrap_servers=f"{host}:{port}",
                auto_offset_reset=auto_offset_reset,
                enable_auto_commit=enable_auto_commit,
                group_id=group_id,
                value_deserializer=lambda x: x.decode("utf-8"),
                # fetch_max_bytes=10 * 1048576, # 10MB
                # max_partition_fetch_bytes=10 * 1048576, # 10MB
                # max_poll_records=200, # 200 messages per poll
            )
            break
        except NoBrokersAvailable:
            print(f"Attempt {i+1} to connect to Kafka server failed")
            time.sleep(5)
    else:
        print("Could not connect to Kafka server after 10 attempts")
        exit(1)

    return consumer


def send_message(
        producer: KafkaProducer,
        message: str,
        topic: str=KAFKA_TOPIC,
    ) -> None:
    """
    Sends a message to a Kafka topic using the provided producer.

    Args:
        producer: The Kafka producer instance.
        message (str): The message to be sent.
        topic (str, optional): The Kafka topic to send the message to. Defaults to KAFKA_TOPIC.

    Returns:
        None
    """
    producer.send(topic, message.encode("utf-8"))
    producer.flush()

    print(f"Published new message")
