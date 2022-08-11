
from threading import Thread


class Analyzer(Thread):
    
    def __init__(self, consumer) -> None:
        Thread.__init__(self)
        
        self.consumer = consumer
        self.consumer.subscribe(topics='topic_BTCUSDT')
        
    def run(self):
        
        for message in self.consumer:
            print("%d:%d: v=%s" % (message.partition,
                                message.offset,
                                message.value))

