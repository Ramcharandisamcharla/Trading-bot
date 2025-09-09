from binance.client import Client
import logging
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Setup logging
logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        """Place a MARKET order"""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logging.info(f"Market Order Response: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a LIMIT order"""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit Order Response: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing limit order: {e}")
            return None
    def check_balance(self, asset="USDT"):
        """Check Futures wallet balance for a given asset"""
        try:
            balances = self.client.futures_account_balance()
            for b in balances:
                if b['asset'] == asset:
                    print(f"Available {asset} Balance:", b['balance'])
                    return float(b['balance'])
            return 0.0
        except Exception as e:
            print(f"Error fetching balance: {e}")
            return 0.0
