from utils import get_consumer


consumer = get_consumer('topic')


for msg in consumer:
    print msg.message.value

consumer.close()
