# pykafka

This is an easy python package to work with Kafka.

## Features

- `get_kafka_producer`
    
    ```python
    from pykafka.utils import get_kafka_producer
    
    producer = get_kafka_producer() # If working between containers
    producer = get_kafka_producer(host="localhost") # If running python locally and kafka inside container
    ```
    
- `get_kafka_consumer`
    
    ```python
    from pykafka.utils import get_kafka_consumer
    
    consumer = get_kafka_consumer() # If working between containers
    consumer = get_kafka_producer(host="localhost") # If running python locally and kafka inside container
    ```
    
- `send_message`
    
    ```python
    from pykafka.utils import send_message
    
    producer = get_kafka_producer()
    send_message(producer, "Hello world")
    ```