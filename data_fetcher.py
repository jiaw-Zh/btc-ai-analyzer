import ccxt
import pandas as pd
from datetime import datetime, timedelta

class BinanceDataFetcher:
    def __init__(self, symbol='BTCUSDT', timeframe='1h'):
        self.exchange = ccxt.binance()
        self.symbol = symbol
        self.timeframe = timeframe
    
    def fetch_ohlcv(self, days=30):
        """Fetch OHLCV data for the specified number of days"""
        try:
            limit = min(1000, days * 24)  # API limit
            ohlcv = self.exchange.fetch_ohlcv(self.symbol, self.timeframe, limit=limit)
            
            df = pd.DataFrame(
                ohlcv,
                columns=['timestamp', 'open', 'high', 'low', 'close', 'volume']
            )
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
    
    def get_latest_price(self):
        """Get the latest price for the trading pair"""
        try:
            ticker = self.exchange.fetch_ticker(self.symbol)
            return ticker['last']
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None
