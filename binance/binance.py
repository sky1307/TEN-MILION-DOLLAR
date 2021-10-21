from binance.client import Client
import csv
client = Client(config.apiKey, config.apiSecret, testnet = True)
print("logged in")

data = client.get_klines(symbol='BTCUSDT', interval= "1h")
with open('data1000d_BTCUSDT.csv','w',newline='') as f:
    writer = csv.writer(f,  delimiter=',')
    writer.writerow(['Open_time','Open','High','Low','Close','Volume','Close_time','Qoute_asset_volume','Number_of_trades','Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Can_be_ignored'])
    for d in data:
        writer.writerow(d)

        
        
   

