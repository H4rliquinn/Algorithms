#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=None):
    if cache == None:
        cache = {}
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) <= 0 and amount > 0:
        return 0
    else:
        if cache.get((amount, denominations[-1]), 0):
            return cache[(amount, denominations[-1])]
        retval1 = making_change(amount-denominations[-1], denominations, cache)
        if not cache.get((amount-denominations[-1], denominations[-1]), 0):
            cache[(amount-denominations[-1], denominations[-1])] = retval1
        retval2 = making_change(amount, denominations[:-1], cache)
        return retval1+retval2


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
