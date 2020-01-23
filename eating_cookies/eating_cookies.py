#!/usr/bin/python

import sys
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def termial(n):
    sum = 0
    if n == 0:
        return 1
    for x in range(n+1):
        sum += x
    return sum


def get_itr(n, depth):
    sum = 0
    if depth == 1:
        return n+1
    ret = get_itr(n, depth-1)
    sum += termial(ret)
    return sum


print(get_itr(3, 1))
print(get_itr(3, 2))
print(get_itr(3, 3))
# print(termial(4))


def eating_cookies(n, cache={0: 1, 1: 1, 2: 2}):
    if n in cache:
        return cache[n]
    else:
        perms = 0
        total = n
        # threes,twos
        for i in range(1, n//3+1):
            print(i, total)
            threes = total//((i)*3)
            # print("Threes", threes)
            total = total-(threes*3)
            # print("total", total)
            twos = total//2
            total = total - (twos*2)
            # print("Twos", twos)
            factorial = math.factorial(twos+threes)
            mults = termial(total, twos+threes)
            # print("Mult", factorial, mults)
            perms += (factorial*mults)
        print("Perms32", perms)
        total = n
        # threes
        for i in range(1, n//3+1):
            threes = total//((i)*3)
            total = total-(threes*3)
            # print("Total3", total)
            factorial = math.factorial(threes)
            mults = termial(total, twos+threes)
            perms += (factorial*mults)
            # print("Mult3", factorial, mults)
        print("Perms3", perms)
        total = n
        # twos
        for i in range(1, n//2+1):
            # print("range2", i)
            twos = total//((i)*2)
            total = total-(twos*2)
            factorial = math.factorial(twos)
            # print("ERR", total)
            mults = termial(total, twos+threes)
            print("Mult2", factorial, mults)
            perms += (factorial*mults)
            print("Perms2", perms)
        # ones
        perms += 1

    return perms


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
