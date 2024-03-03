import time
from pykafka.utils import (
    get_kafka_producer,
    send_message,
)





if __name__ == "__main__":
    try:
        producer = get_kafka_producer() # Create a producer
        published_messages = 0 # Counter for published messages

        # Loop to publish messages to the topic
        while True:
            send_message(producer, f"Message {published_messages}")
            published_messages += 1

            time.sleep(5)
    except KeyboardInterrupt:
        print("Shutting down producer")
        producer.close()

        exit(0)
