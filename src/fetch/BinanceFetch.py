
import datetime
import json
from DataStructure import TradeDataStructure
from Fetch import Fetch
from binance.client import Client
import pandas as pd

class BinanceFetch(Fetch):

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
        
        print("[*] Get the data")
        print(df_data)
        
        ## Preprocess the data
        numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
        df_data[numeric_columns] = df_data[numeric_columns].apply(pd.to_numeric, axis = 1)

        df_data = df_data.set_index(df_data["Open time"])
        # df_data.index = pd.to_datetime(df_data.index, unit = "ms")
        df_data = df_data.drop("Open time", axis=1)

        ## Save the assets and the metadata
        data = TradeDataStructure(df_data)
        print(data.get_data())
        
        data_json = data.to_json()
        
        print(data_json)
                
        self.sended(data_json)
        
        
    def sended(self, data):
        print("[*] Send the data to kafka")
        
        data = json.dumps(data)#, indent=4, sort_keys=True, default=str)
   
        for i in range(100):
    
            self.producer.send(
                topic= "topic_BTCUSDT",
                partition=0,
                value={"schema":{"type":"struct","fields":[{"type":"boolean","optional":False,"field":"flag"},{"type":"int8","optional":False,"field":"id8"},{"type":"int16","optional":False,"field":"id16"},{"type":"int32","optional":False,"field":"id32"},{"type":"int64","optional":False,"field":"id64"},{"type":"float","optional":False,"field":"idFloat"},{"type":"double","optional":False,"field":"idDouble"},{"type":"string","optional":True,"field":"msg"}],"optional":False,"name":"msgschema"},"payload":{"flag":False,"id8":222,"id16":222,"id32":222,"id64":222,"idFloat":222,"idDouble":333,"msg":"hi"}}
            )
            self.producer.flush()
            
            
            print("send !")
            import time
            time.sleep(10)
            
            
        
        print("[*] Sended !")
    
    
if __name__ == "__main__":
    
    
    fetcher = BinanceFetch(host="localhost", port=9092, pair="BTCUSDT")
    
    print("Loading data...")
    
    fetcher.fetch()
    
        