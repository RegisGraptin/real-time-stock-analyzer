
import json

from abc import ABCMeta
from kafka import KafkaProducer

class Fetch(metaclass=ABCMeta):
    
    def __init__(self, host: str, port: str) -> None:
        
        # TODO :: Create a fabric pattern for the creation of this producer
        
        # Create a kafka producer
        self.producer = KafkaProducer(
            bootstrap_servers = [f"{host}:{port}"],
            api_version=(0,10,2),
            value_serializer  = lambda v: json.dumps(v).encode('utf-8')
        )
        
    def fetch(self):
        pass
    
    def send(self):
        pass


