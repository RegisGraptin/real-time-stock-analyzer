from kafka import KafkaConsumer
from kafka import TopicPartition

import json

import os
from dotenv import load_dotenv



def create_consumer(id: int = 0):
    
    host = os.environ.get("HOST")
    port = os.environ.get("PORT")

    print(f"{host}:{port}")

    return KafkaConsumer(
        "btc-price",
        
        # group_id = str(id) + "_partitioned",
        
        
        api_version=(0,10,2),
        
        bootstrap_servers = f"{host}:{port}",
        # auto_offset_reset='earliest',
        
        # security_protocol = "SSL",
        
        # ssl_cafile        = os.environ.get("SSL_CA"),
        # ssl_certfile      = os.environ.get("SSL_CERT"),
        # ssl_keyfile       = os.environ.get("SSL_KEY"),
        # ssl_password      = os.environ.get("SSL_PASSWORD"),
      
        value_deserializer = lambda v: json.loads(v.decode('utf-8')),
        
        auto_offset_reset='earliest',
    )



if __name__ == "__main__":
    
    # Load local environment
    load_dotenv()

    consumer = create_consumer()
    
    # consumer.assign([TopicPartition("hotel-booking-request", 1)])

    consumer.subscribe(topics='topic_BTCUSDT')

    print("Waiting...")
    for message in consumer:
        
        print ("%d:%d: v=%s" % (message.partition,
                            message.offset,
                            message.value))

    # consumer.assign([TopicPartition("hotel-booking-request", 1)])
    # consumer.subscription()
    # for message in consumer:
    #     print ("p=%d o=%d value=%s" % (message.partition,
    #                                 message.offset,
    #                                 message.value))
