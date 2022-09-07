
import os

from dotenv import load_dotenv

from data.KafkaFactory import KafkaFactory
from fetch.BinanceFetch import BinanceFetch
from trade.PriceAlert import PriceAlert
from trade.Analyzer import Analyzer

class Manager:
    
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        
        self.kafkaFactory = KafkaFactory(self.host, self.port)

    def run_data_producer(self):
        
        # TODO :: Have a config file and loop for each requiere configuration 
        
        fetcherBTC = BinanceFetch(host=self.host, port=self.port, pair="BTCUSDT")
        
        print("Run the data thread...")
        
        # Run all thread
        fetcherBTC.start()
        
        

        # print("Run the analyzer...")
        
        # analyzer = Analyzer(self.kafkaFactory.consumer("topic_BTCUSDT"))
        # analyzer.start()
        
        print("Price alert on BTC...")
        priceAlert = PriceAlert(self.kafkaFactory.consumer("topic_BTCUSDT"))
        priceAlert.start()
        
        


if __name__ == "__main__":
   
   # Load local environment
   load_dotenv()
   
   host = os.environ.get("HOST")
   port = os.environ.get("PORT")
   
   manager = Manager(host, port)
   manager.run_data_producer()
   
   
