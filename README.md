
# Gather data from different APIs








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








