
# Real-Time Stock Analysis 

With the surge of crypto-currencies, finance has becoming more and more accessible for a larger public.
Data are the key and are now accessible. In this project, we present a simple architecture allowing us to gather a large amount of data through different api/services. We allow the possibility to save those data and to use them directly for real-time purpose. 


## Getting start


Launch all the components
```bash
sudo docker-compose up 

curl -X POST -H "Accept:application/json" -H "Content-Type:application/json" --data @config/connector.json http://localhost:8083/connectors

```

## Fetch the data from binance each minute

```bash 
export PYTHONPATH="${PYTHONPATH}:./src/"
python3 ./src/manager.py
```









## Architecture

https://questdb.io/blog/2022/06/07/data-pipeline-with-kafka-and-questdb/



Currently focus on crypto-currencies, 
Gather trading data using different apis. 
We decompose our system by using kafka system.





## Links

Tutorial : 

https://redpanda.com/blog/real-time-crypto-tracker-questdb-redpanda

https://github.com/Yitaek/kafka-crypto-questdb


curl -X POST -H "Accept:application/json" -H "Content-Type:application/json" --data @config/connector.json http://localhost:8083/connectors

curl -G \
  --data-urlencode "query=select * from 'Binance_BTCUSDT'" \
  http://localhost:9000/exp


localhost:8083/connectors/postgres-sink-btc

curl -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
--data @config/connector.json http://localhost:8083/connectors








