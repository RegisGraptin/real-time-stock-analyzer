
import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

class KafkaFactory: 
    
    def __init__(self, host: str, port: str) -> None:
        self.host = host
        self.port = port
        
        self.api_version = (0,10,2)
    
    
    # topic = "btc-price",
    def consumer(self, topic: str, id: int = 0):
        return KafkaConsumer(
            topic,
            # group_id = str(id) + "_partitioned",
            
            api_version = self.api_version,
            bootstrap_servers = f"{self.host}:{self.port}",
            
            # security_protocol = "SSL",
            
            # ssl_cafile        = os.environ.get("SSL_CA"),
            # ssl_certfile      = os.environ.get("SSL_CERT"),
            # ssl_keyfile       = os.environ.get("SSL_KEY"),
            # ssl_password      = os.environ.get("SSL_PASSWORD"),
        
            value_deserializer = lambda v: json.loads(v.decode('utf-8')),
            
            auto_offset_reset='earliest',
        )
        
        
    def producer(self):
        return KafkaProducer(
            bootstrap_servers = [f"{self.host}:{self.port}"],
            api_version=self.api_version,
            value_serializer  = lambda v: json.dumps(v).encode('utf-8')
        )