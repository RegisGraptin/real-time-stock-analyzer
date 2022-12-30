
import json

from abc import ABCMeta
from kafka import KafkaProducer

from threading import Thread

from data.KafkaFactory import KafkaFactory
from data.DataStructure import DataStructure

class Fetcher(Thread, metaclass=ABCMeta):
    
    def __init__(self) -> None:
        Thread.__init__(self)
        
        # Get a Kafka Producer
        self.producer = KafkaFactory().producer()
        
    def fetch(self) -> DataStructure:
        """Fetch the data."""
        pass
    
    def send(self, data: DataStructure):
        """Send the data to the kafka producer.

        Args:
            data (_type_): _description_
        """
        pass
    
    def run(self):
        """Run the thread process."""
        pass


