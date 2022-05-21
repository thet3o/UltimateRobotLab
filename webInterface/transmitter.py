import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='commands')
    
def sendCmd(command):
    channel.basic_publish(exchange='', routing_key='commands', body=command)
    print("Command sent: " + str(command))    
    