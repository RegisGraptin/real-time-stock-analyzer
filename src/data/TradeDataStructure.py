
import pandas as pd

from data.DataStructure import DataStructure

class TradeDataStructure(DataStructure):

    LABELS = ['Open', 'Close', 'High', 'Low', 'Volume']

    def __init__(self, df: pd.DataFrame) -> None:
        super().__init__(df)

    def get_data(self):
        return self.df[self.LABELS]

    def to_json(self):
        
        data = {
            "schema": {
                "type": "struct",
                "fields": [
                        {"type": "int32", "optional": False, "field": "timestamp"},
                        {"type": "float", "optional": False, "field": "open"},
                        {"type": "float", "optional": False, "field": "close"},
                        {"type": "float", "optional": False, "field": "high"},
                        {"type": "float", "optional": False, "field": "low"},
                        {"type": "float", "optional": False, "field": "volume"},
                ],
                "optional": False, 
                "name": "msgschema"
            },
            "payload": {
                "timestamp": int(self.df.index.values[0]),
                "open"     : self.df["Open"].values[0],
                "close"    : self.df["Close"].values[0],
                "high"     : self.df["High"].values[0],
                "low"      : self.df["Low"].values[0],
                "volume"   : self.df["Volume"].values[0]
            }
        }
        
        return data
