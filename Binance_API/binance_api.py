from binance.client import Client
import yaml
import csv


class Binance():
    with open("config/binance.yaml", 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    apikey = config['apiKey']
    apiSecret = config['apiSecret']
    symbol = config['symbol']
    interval = config['interval']
    limit = config['limit']
    data_file = config['data_file']
    data_dir = config['data_dir']

    def __init__(self):
        self.client = Client(Binance.apiKey, Binance.apiSecret, testnet=True)

    def get_data(self):
        data = self.client.get_klines(symbol=Binance.symbol, interval=Binance.interval, limit=Binance.limit)
        dir_file_data = Binance.data_dir + Binance.data_file
        with open(dir_file_data, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Qoute_asset_volume',
                             'Number_of_trades', 'Taker_buy_base_asset_volume', 'Taker_buy_quote_asset_volume',
                             'Can_be_ignored'])
            for d in data:
                writer.writerow(d)
        return

if __name__=="__main__":
    BI = Binance()
    BI.get_data()




        
        
   

