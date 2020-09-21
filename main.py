import requests
import pandas as pd
import io
# class for TradingBot
class TradeBot():
    def __init__(self, *arg):
        self.symbol = arg
        for s in self.symbol:
            response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={s}&apikey=demo&datatype=csv&interval=30min&slice=year1month1").content
            responseData = pd.read_csv(io.StringIO(response.decode('utf-8')))

            # print(responseData)
            mean = sum(responseData['close']) / len(responseData['close'])

            buy = []
            sell = []
            flat = []

            time = list(responseData['time'])
            close = list(responseData['close'])

            for i in time:
                for x in close:
                    if x > mean:
                        buy.append(f"{s} {i} {x} buy")
                    elif x < mean:
                        sell.append(f"{s} {i} {x} sell")
                    else:
                        flat.append(f"{s} {i} {x} flat")

            trades = {'BUY' : buy, 'SELL' : sell, 'FLAT' : flat}
            print(trades)


TradeBot("spy","tsla","ibm")
TradeBot("googl", "msft", "aapl")