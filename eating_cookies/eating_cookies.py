#!/usr/bin/python

import sys
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def termial(n):
    sum = 0
    for x in range(n+1):
        sum += x
    return sum


def eating_cookies(n, cache={0: 0, 1: 1, 2: 2}):
    if n in cache:
        return cache[n]
    else:
        perms = 0
        total = n
        # threes
        for i in range(n//3):
            print(i, total)
            threes = total//((i+1)*3)
            print("Threes", threes)
            total = total-(threes*3)
            print("total", total)
            twos = total//2
            total = total - (twos*2)
            print("Twos", total, twos)
            factorial = math.factorial(twos+threes)
            mults = termial(total+1)
            print("Mult", mults)
            perms += (factorial*mults)+1
        # twos
        for i in range(n//2):
            twos = total//((i+1)*2)
            total = total-(twos*2)
            factorial = math.factorial(twos)
            mults = termial(total+1)
            perms += (factorial*mults)+1
    return perms


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
