import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello2', body='Hello Ada!')
print('[x] Mensagem Enviada')
connection.close()
