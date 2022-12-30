
from binance.client import Client
from data.TradeDataStructure import TradeDataStructure

import pandas as pd

from .API import API

class BinanceAPI(API):
    
    STARTING_DATE = "30 July 2022"
    INTERVAL      = Client.KLINE_INTERVAL_1MINUTE
    
    def __init__(self) -> None:
        self.client = Client()
    
    
    def get_data(self, pair: str, interval: str = INTERVAL, when: str = "1 minute ago UTC") -> TradeDataStructure:
    
        klinesT = self.client.get_historical_klines(pair, interval, when)
        
        columns = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"]

        df_data = pd.DataFrame(klinesT, columns=columns)
        
        ## Preprocess the data
        numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
        df_data[numeric_columns] = df_data[numeric_columns].apply(pd.to_numeric, axis = 1)

        df_data.rename(columns={
            "Open"  : "open", 
            "High"  : "high",
            "Low"   : "low",
            "Close" : "close",
            "Volume": "volume"
        })
        
        df_data = df_data.set_index(df_data["Open time"])
        
        # Reduce the timestamps in second instead of ms
        df_data.index = df_data.index / 1000
        
        # df_data.index = pd.to_datetime(df_data.index, unit = "ms")
        df_data = df_data.drop("Open time", axis=1)

        ## Save the assets and the metadata
        data = TradeDataStructure(df_data)
        
        return data