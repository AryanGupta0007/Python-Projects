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

        get_Data = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=ETHBTC").json()
        price = get_Data["price"]
        prices.append(price)
        # greatest_value = store_highest_value(price)    
        if (price == "0.06875000"):
            print("you should consider buying")
        else:
            print(get_Data, end = "\r") # carriage return used to return the curson of the mouse to the initial position
        
        if (keyboard.is_pressed("s")):
            os.system("cls")
            print(f"{price_stats(prices)}")
        
        
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
    
    highest_price = current_price
    return f"highest_price: {highest_price}\nlowest_price: {lowest_price}"

        
if __name__ == "__main__":
    main()    