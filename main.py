from bot import BasicBot

def main():
    bot = BasicBot()

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    if order_type == "LIMIT":
        price = float(input("Enter limit price: "))
        order = bot.place_limit_order(symbol, side, quantity, price)
    else:
        order = bot.place_market_order(symbol, side, quantity)

    print("Order Response:", order)

if __name__ == "__main__":
    main()