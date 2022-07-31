
import os
from kafka import KafkaProducer
import json
import datetime

from dotenv import load_dotenv


def create_producer():
   
   host = os.environ.get("HOST")
   port = os.environ.get("PORT")
   
   return KafkaProducer(
      
      bootstrap_servers = [f"{host}:{port}"],
      # security_protocol = "SSL",
      api_version=(0,10,2),
      # ssl_cafile        = os.environ.get("SSL_CA"),
      # ssl_certfile      = os.environ.get("SSL_CERT"),
      # ssl_keyfile       = os.environ.get("SSL_KEY"),
      # ssl_password      = os.environ.get("SSL_PASSWORD"),
      value_serializer  = lambda v: json.dumps(v).encode('utf-8')
   )


if __name__ == "__main__":
   
   # Load local environment
   load_dotenv()
   
   
   producer = create_producer()

   print("Send")

   producer.send(
      'hotel',  
      {
         "timestamps": "07-07-2021",
         "low": 125.25,
         "high": 157.8,
         "open": 127.3,
         "close": 128.6
      }
   )
   
   data = {
              "schema": {
                "type": "struct",
                "fields": [
                  {
                    "type": "string",
                    "optional": False,
                    "field": "currency"
                  },
                  {
                    "type": "float",
                    "optional": False,
                    "field": "amount"
                  },
                  {
                    "type": "string",
                    "optional": False,
                    "field": "timestamp"
                  }
                ],
                "optional": False,
                "name": "coinbase"
              },
              "payload": {
                "timestamp": datetime.datetime.now(),
                "currency": "ETH",
                "amount": 125.5
              }
            }    
   
   data = json.dumps(data, indent=4, sort_keys=True, default=str)
   
   data = {"schema":{"type":"struct","fields":[{"type":"boolean","optional":False,"field":"flag"},{"type":"int8","optional":False,"field":"id8"},{"type":"int16","optional":False,"field":"id16"},{"type":"int32","optional":False,"field":"id32"},{"type":"int64","optional":False,"field":"id64"},{"type":"float","optional":False,"field":"idFloat"},{"type":"double","optional":False,"field":"idDouble"},{"type":"string","optional":True,"field":"msg"}],"optional":False,"name":"msgschema"},"payload":{"flag":False,"id8":222,"id16":222,"id32":222,"id64":222,"idFloat":222,"idDouble":333,"msg":"hi"}}
   
   producer.send(
      "topic_BTCUSDT",
      data
   )
   
   
   
   
   print("flush ?")
   producer.flush()
   
   
