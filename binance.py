import requests
import json
import keyboard
import sys
import os

    
def main():
    print("Press \"Q\" to exit the program")
    print("Press \"S\" to see the price stats")
    prices = []

    while True:

        get_Data = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT").json()
        price = get_Data["price"]
        symbol = get_Data["symbol"]
        current_price = float(price)
        prices.append(price)
        # greatest_value = store_highest_value(price)    
        if (price == "1500"):
            print(f"you should consider buying the current price is ${round(current_price, 2)}")
        else:
            print(f"Symbol: {symbol} Current Price: ${round(current_price, 2)}", end = "\r")
            
             # carriage return used to return the curson of the mouse to the initial position
        # print(price_stats(prices))
        if (keyboard.is_pressed("s")):
            os.system("cls")
            print(price_stats(prices))

        
        if (keyboard.is_pressed("q")):
            os.system("cls")
            print(price_stats(prices))
            break

def price_stats(prices):
    current_price = prices[0]
    lowest_price = prices[0]
        
    for x in range(1, len(prices)):
        if (current_price < prices[x]):
            current_price = prices[x]
    
    for x in range(1, len(prices)):
        if (lowest_price > prices[x]):
            lowest_price = prices[x]
    lowest_price = float(lowest_price)
    highest_price = float(current_price)
    return f"highest_price: ${round(highest_price, 2)}\nlowest_price: ${round(lowest_price, 2)}\nPress S to update"


        
if __name__ == "__main__":
    main()    