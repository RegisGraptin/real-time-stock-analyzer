

from data.TradeDataStructure import TradeDataStructure
from api.API import API
from fetch.Fetcher import Fetcher
from binance.client import Client
from data.DataStructure import DataStructure
import pandas as pd
import datetime
import time

class APIFetcher(Fetcher):
    """API Fetcher

    Notes : All time and timestamp related fields are in milliseconds.

    Args:
        Fetch (_type_): _description_
    """

    STARTING_DATE = "30 July 2022"
    INTERVAL      = Client.KLINE_INTERVAL_1MINUTE
    
    def __init__(self, api: API, pair: str) -> None:
        super().__init__()

        self.api  = api
        self.pair = pair
        
    
    
    def fetch(self):
        
        data = self.api.get_data(self.pair)
        
        return data
        
        
    def send(self, data: DataStructure):
   
        self.producer.send(
                topic= "topic_" + self.pair,
                partition=0,
                value=data.to_json()
            )
        self.producer.flush()
    
    
    def run(self):

        while True:
            
            # Fetch the data and send them to kafka
            print("-- Fetch data")
            data = self.fetch()
            print(data)
            print("-- End Fetch")
            self.send(data)
            
            # Wait the next minute
            sleeptime = 60 - datetime.datetime.utcnow().second
            time.sleep(sleeptime)
