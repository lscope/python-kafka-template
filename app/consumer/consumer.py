from pykafka.utils import get_kafka_consumer




if __name__ == "__main__":
    try:
        consumer = get_kafka_consumer() # Create a consumer

        # Loop to consume messages from the topic
        while True:
            msg = consumer.poll() # Poll messages

            # If messages are received, print them
            if msg:
                for _, messages in msg.items():
                    for i, message in enumerate(messages):
                        print(f"Received message {i}: {message.value}")

    except KeyboardInterrupt:
        print("Shutting down consumer")
        consumer.close()

        exit(0)
