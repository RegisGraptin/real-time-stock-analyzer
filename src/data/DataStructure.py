
import pandas as pd

class DataStructure:
    """Data structure class.
    Allow to have a class regrouping the different information about the data.
    """

    def __init__(self, df: pd.DataFrame) -> None:

        # TODO :: Maybe add metadata information

        self.df = df

    # def save(self, path) -> None:
    #     self.df.to_csv(path + ".csv")

    def get_data(self):
        return self.df

    def add_data(self, df_add) -> None:
        self.df = self.df.merge(df_add)
        return self


