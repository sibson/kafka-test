from utils import get_consumer


COUNT = 1000

consumer = get_consumer('topic')


for ix, msg in enumerate(consumer):
    if ix % COUNT == 0:
        print ix, msg.message.value

consumer.close()
