# -*- coding: utf-8 -*-
# JIAHE CHEN   2019/03/18
# For this exercise, I use the python 3.7.
import pandas as pd


# two functions to calculate the best method to buy and sell
# 1.As the requested, I use the 20 million dollars as the executed quantity for buying
#   and 12 million dollars as the executed quantity for selling.
#
# 2.All the transaction will be in increments of 1, 3, and 5 million dollars.
#
# 3.I use two dictionaries to represent the results. The results show which quotes we
#   should trade to fully execute the buy and sell trades against the best average price.
#   I also put the quantity of every trade in the dictionary. Since we are only allowed to
#   take these quotes in increments of 1, 3, and 5 million dollars, some quotes have been
#   taken more than once. For example, the number 17 (Ask  FX_HOTSPOT_FIRM  1.15184  6000000)
#   has been taken in increments of 1 and 5 million dollars.
#   

def buy(amount):
    buy_method = {}
    for key, values in buy_quotes.items():

        if values < amount:
            amount -= values
            buy_method[key] = []
            while values > 5000000:
                buy_method[key].append(5000000)
                values -= 5000000
            if values == 1000000 or values == 3000000 or values == 5000000:
                buy_method[key].append(values)
            elif values == 2000000:
                buy_method[key].append(1000000)
                buy_method[key].append(1000000)
            elif values == 4000000:
                buy_method[key].append(3000000)
                buy_method[key].append(1000000)


        else:
            buy_method[key] = []
            while amount >= 5000000:
                buy_method[key].append(5000000)
                amount -= 50000000
            if amount == 1000000 or amount == 3000000:
                buy_method[key].append(amount)
            elif amount == 2000000:
                buy_method[key].append(1000000)
                buy_method[key].append(1000000)

            elif amount == 4000000:
                buy_method[key].append(3000000)
                buy_method[key].append(1000000)

            return buy_method





def sell(amount):
    sell_method = {}
    for key, values in sell_quotes.items():

        if values < amount:
            amount -= values
            sell_method[key] = []
            while values > 5000000:
                sell_method[key].append(5000000)
                values -= 5000000
            if values == 1000000 or values == 3000000 or values == 5000000:
                sell_method[key].append(values)
            elif values == 2000000:
                sell_method[key].append(1000000)
                sell_method[key].append(1000000)
            elif values == 4000000:
                sell_method[key].append(3000000)
                sell_method[key].append(1000000)


        else:
            sell_method[key] = []
            while amount > 5000000:
                sell_method[key].append(5000000)
                amount -= 50000000
            if amount == 1000000 or amount == 3000000 or amount == 5000000:
                sell_method[key].append(amount)
            elif amount == 2000000:
                sell_method[key].append(1000000)
                sell_method[key].append(1000000)
            elif amount == 4000000:
                sell_method[key].append(3000000)
                sell_method[key].append(1000000)

            return sell_method






if __name__ == "__main__":
    print('Jiahe Chen, Pragma exercise')
    # read the data
    df = pd.read_csv('C:\\Users\\paulchan\\Desktop\\3.csv')

    # divide into buy and sell parts
    dbuy = df[df['Side'] == 'Ask']
    dsell = df[df['Side'] == 'Bid']

    dbuy.head(5)
    dsell.head(5)

    # transform the dataframe into lists and dictionaries
    buylist_Qty = dbuy['Qty'].tolist()
    buylist_Price = dbuy['Price'].tolist()
    selllist_Qty = dsell['Qty'].tolist()
    selllist_Price = dsell['Price'].tolist()

    # make two dictionaries for the prices and Qty of two sides(ask, bid)
    print(buylist_Price)
    print("Quantity of Available Buy Orders: %s" % buylist_Qty)

    buy_quotes = {}
    sell_quotes = {}

    for i in range(len(buylist_Price)):
        buy_quotes[buylist_Price[i]] = buylist_Qty[i]
    print(" Buy Quotes: %s" % buy_quotes)

    for i in range(len(selllist_Price)):
        sell_quotes[selllist_Price[i]] = selllist_Qty[i]
    print(" Sell Quotes: %s" % sell_quotes)


    buy_order = buy(20000000)

    sell_order = sell(12000000)
    print("-----------------------------------------")
    print("The best buy method is: %s" % buy_order)
    print("The best sell method is: %s" % sell_order)
    print("-----------------------------------------")
