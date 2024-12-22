import ccxt

# Initialize the exchange (Binance in this example)
exchange = ccxt.binance()

# Fetch ticker data for Bitcoin (BTC/USDT)
ticker = exchange.fetch_ticker('BTC/USDT')

# Display the result
print(f"Symbol: {ticker['symbol']}")
print(f"Last Price: {ticker['last']}")
print(f"High Price: {ticker['high']}")
print(f"Low Price: {ticker['low']}")
