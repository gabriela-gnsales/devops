from redis import StrictRedis
from time import strftime, sleep

client = StrictRedis(host="localhost", port=6379)

subscriber = client.pubsub()
subscriber.psubscribe('channel_test')

while True:
    messages = subscriber.get_message()
    now = strftime('%d/%m/%Y:%H:%M:%S')

    if messages:
        print(f'{now} - {messages["data"]}')
    else:
        print(f'{now} - Nothing here!!!')
    sleep(1)