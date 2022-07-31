

import pandas as pd


class DataFrameStructure:
    """Data structure class.
    Allow to have a class regrouping the different information about the data.
    """

    def __init__(self, df: pd.DataFrame) -> None:

        # TODO :: Maybe add metadata information

        self.df = df

    def save(self, path) -> None:
        self.df.to_csv(path + ".csv")

    def get_data(self):
        return self.df

    def add_data(self, df_add) -> None:
        self.df = self.df.merge(df_add)
        return self


class TradeDataStructure(DataFrameStructure):

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
                        {"type": "long", "optional": False, "field": "timestamp"},
                        {"type": "float", "optional": False, "field": "open"},
                        {"type": "float", "optional": False, "field": "close"},
                        {"type": "float", "optional": False, "field": "high"},
                        {"type": "float", "optional": False, "field": "low"},
                        {"type": "float", "optional": False, "field": "volume"},
                ],
                "optional": False, "name": "trade"
            },
            "payload": {
                "timestamp": int(self.df.index.values[0]),
                "open": self.df["Open"].values[0],
                "close": self.df["Close"].values[0],
                "high": self.df["High"].values[0],
                "low": self.df["Low"].values[0],
                "volume": self.df["Volume"].values[0],
            }
        }
        
        return data
