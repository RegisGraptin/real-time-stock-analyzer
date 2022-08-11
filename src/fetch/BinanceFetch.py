
import json
from data.TradeDataStructure import TradeDataStructure
from fetch.Fetch import Fetch
from binance.client import Client
import pandas as pd
import datetime
import time

class BinanceFetch(Fetch):
    """Binance api

    Notes : All time and timestamp related fields are in milliseconds.

    Args:
        Fetch (_type_): _description_
    """

    STARTING_DATE = "30 July 2022"
    INTERVAL      = Client.KLINE_INTERVAL_1MINUTE
    
    def __init__(self, host: str, port: str, pair: str) -> None:
        super().__init__(host, port)

        # Create binance client
        self.client = Client()
        
        self.pair = pair
    
    
    def fetch(self):
        
        # Get the data
        klinesT = self.client.get_historical_klines(self.pair, BinanceFetch.INTERVAL, "1 minute ago UTC")
        
        columns = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"]

        df_data = pd.DataFrame(klinesT, columns=columns)
        
        ## Preprocess the data
        numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
        df_data[numeric_columns] = df_data[numeric_columns].apply(pd.to_numeric, axis = 1)

        df_data = df_data.set_index(df_data["Open time"])
        
        # Reduce the timestamps in second instead of ms
        df_data.index = df_data.index / 1000
        
        # df_data.index = pd.to_datetime(df_data.index, unit = "ms")
        df_data = df_data.drop("Open time", axis=1)

        ## Save the assets and the metadata
        data = TradeDataStructure(df_data)
        
        data_json = data.to_json()
        
        self.send(data_json)
        
        
    def send(self, data: dict):
   
        if data == None:
            print("[Error] None value for data")
            return
        else:
            print("[Info] New value sended")
            
        self.producer.send(
                topic= "topic_BTCUSDT",
                partition=0,
                value=data
            )
        self.producer.flush()
    
    
    def run(self):

        while True:
            
            # Fetch the data and send them to kafka
            data = self.fetch()
            self.send(data)
            
            # Wait the next minute
            sleeptime = 60 - datetime.datetime.utcnow().second
            time.sleep(sleeptime)


if __name__ == "__main__":
    
    
    fetcher = BinanceFetch(host="localhost", port=9092, pair="BTCUSDT")
    fetcher.run()
    
        