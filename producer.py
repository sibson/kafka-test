from datetime import datetime

from utils import get_producer


producer = get_producer()

while True:
    producer.send_messages('topic', 'Its now {}'.format(datetime.now()))
