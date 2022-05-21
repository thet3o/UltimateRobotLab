from threading import Thread
import pika

class Receiver(Thread):
    
    def callback(ch, method, properties, body):
        print("Command received: " + str(body))
        #pass
        
    def listener():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='commands')

        channel.basic_consume('commands', Receiver.callback)
        channel.start_consuming()

    