from abc import ABCMeta

from data.DataStructure import DataStructure

class API(metaclass=ABCMeta):
    
    def __init__(self) -> None:
        pass
    
    
    def get_data(self, pair: str, interval: str, when: str) -> DataStructure:
        """Get the data from the API.

        Args:
            pair (str): Pair of value we want to extract.
            interval (str): Time interval for each trade.
            when (str): From what range do we gather the data.

        Returns:
            DataStructure: Extracted data.
        """
        pass

