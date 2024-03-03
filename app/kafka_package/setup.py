from setuptools import setup, find_packages





setup(
    name="pykafka",
    description="A simple kafka package to produce and consume messages",
    version="0.0.0",
    packages=find_packages(exclude=["test", "consumer", "producer"]),
    install_requires=[
        "kafka-python",
    ],
)