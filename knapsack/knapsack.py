#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def ratio_sort(i):
    return i.value/i.size


def knapsack_solver(items, capacity):
    chosen_items = []
    missed_list = []
    value_list = items.copy()
    value_list.sort(key=ratio_sort, reverse=True)
    value = 0

    for i in range(len(value_list)):
        if value_list[i].size <= capacity:
            chosen_items.append(value_list[i].index)
            capacity = capacity-value_list[i].size
            value += value_list[i].value
        else:
            missed_list.append(value_list[i])
        if capacity == 0:
            break
    for missed in missed_list:
        for previous in range(len(chosen_items)-2, 0, -1):
            if items[chosen_items[-1]-1].size+capacity+items[chosen_items[previous]-1].size >= missed.size:
                if items[chosen_items[-1]-1].value+items[chosen_items[previous]-1].value < missed.value:
                    print("SUCCESS!", missed.value,
                          items[chosen_items[-1]-1].value, items[chosen_items[previous]-1].value)
                    value += missed.value - \
                        (items[chosen_items[-1]-1].value +
                         items[chosen_items[previous]-1].value)
                    chosen_items.pop(previous)
                    chosen_items.pop()
                    chosen_items.append(missed.index)
    return {'Value': value, 'Chosen': sorted(chosen_items)}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
