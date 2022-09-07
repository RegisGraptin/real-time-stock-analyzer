
from threading import Thread

from data.TradeDataStructure import TradeDataStructure


class PriceAlert(Thread):
    
    def __init__(self, consumer) -> None:
        Thread.__init__(self)
        
        self.consumer = consumer
        self.consumer.subscribe(topics='topic_BTCUSDT')
        
    def run(self):
        
        for message in self.consumer:
            # print("%d:%d: v=%s" % (message.partition,
            #                     message.offset,
            #                     message.value))
            
            kafka_message = message.value
            
            if kafka_message:
                tradeData = TradeDataStructure.create_json(kafka_message)
                
                closePrice = tradeData.get_data().close.iat[0]
                
                if closePrice > 23000.00:
                    print("Sell process, price at :", closePrice)
                

