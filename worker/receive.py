#!/usr/bin/env python
import pika
import pymongo
from test.main import collection
# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Set up MongoDB connection
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["iot_data_db"]
# collection = db["iot"]

# Declare queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the exchange
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # Insert the received message into MongoDB
    collection.insert_one({"message": body.decode()})

    print(" [x] Message inserted into MongoDB:", body)

# Set up consumer
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Start consuming messages
channel.start_consuming()
