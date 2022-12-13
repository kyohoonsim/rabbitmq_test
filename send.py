import pika

credentials = pika.PlainCredentials('admin', 'admin')
parameters =  pika.ConnectionParameters('localhost', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                    routing_key='hello',
                    body='hello world!')

print(" [x] sent 'Hello World!' ")

connection.close()