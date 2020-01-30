#!/usr/bin/python
import random
import argparse


def last_index(arr, el):
    indexPosList = []
    indexPos = 0
    while True:
        try:
            indexPos = arr.index(el, indexPos)
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
    return indexPosList[-1]


def find_max_profit(prices):
    sorted_prices = prices.copy()
    sorted_prices.sort()
    low = 0
    high = len(prices)-1
    last_change = None
    while True:
        print("start", low, high, last_change)
        if prices.index(sorted_prices[low]) < last_index(prices, sorted_prices[high]):
            break
        if last_change == 'h':
            for i in range(0, low):
                print("high", low, i, high)
                if prices.index(sorted_prices[i]) < last_index(prices, sorted_prices[high]):
                    break
        elif last_change == 'l':
            for i in range(len(prices)-1, high, -1):
                print("low", low, i, high)
                if prices.index(sorted_prices[low]) < last_index(prices, sorted_prices[high]):
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
