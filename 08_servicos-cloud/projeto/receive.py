import sys, pika, os

def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '5672'))

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print('[x] Mensagem recebida', body)
        print(ch, 'method: ', method, 'properties: ', properties)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print('[x] Aguardando mais mensagens. Aperte CTRL+C para sair.')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        receive_message()
    except KeyboardInterrupt:
        print('Interrompendo terminal')
        try:
            sys.exit(0)
        except SystemExit:
            os.exit(0)