import os
import json

from kafka import KafkaClient, SimpleProducer, SimpleConsumer


def parse_url():
    settings = json.loads(os.environ.get('KAFKA_URL'))

    return settings


def get_client(settings=None):
    if settings is None:
        settings = parse_url()

    kafka = KafkaClient(settings['kafka'])

    return kafka


def get_producer():
    producer = SimpleProducer(get_client())

    return producer


def get_consumer(topic):
    ident = 'WHOOPS'
    consumer = SimpleConsumer(get_client(), ident, topic)
    return consumer
