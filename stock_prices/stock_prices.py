#!/usr/bin/python
import random
import argparse


def find_max_profit(prices):
    sorted_prices = prices.copy()
    sorted_prices.sort()
    low = 0
    high = len(prices)-1
    last_change = None
    while True:
        # print(low, high, last_change)
        if prices.index(sorted_prices[low]) < prices.index(sorted_prices[high]):
            # print(prices.index(sorted_prices[low]))
            break
        if last_change == 'h':
            x = 0
            y = low-2
            z = 1
        elif last_change == 'l':
            x = len(prices)-1
            y = high+2
            z = -1
        if last_change != None:
            for i in range(x, y, z):
                if prices.index(sorted_prices[low]) < prices.index(sorted_prices[high]):
                    break
        if sorted_prices[low+1]-sorted_prices[low] >= sorted_prices[high]-sorted_prices[high-1]:
            high -= 1
            last_change = 'h'
        else:
            low += 1
            last_change = 'l'
    return prices[prices.index(sorted_prices[high])]-prices[prices.index(sorted_prices[low])]


# arr5 = random.sample(range(1500000), 200000)
# print(find_max_profit(arr5))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
