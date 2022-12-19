#!/usr/bin/env python3

import json
from functools import cmp_to_key

def main():
    data = []
    with open("input.txt", "r") as file:
        data = [json.loads(line.strip()) for line in file if line != '\n']

    """
    Part 1:
    Compare each set of two lists using recursion and sum up every group
    where first list is "less-than" right
    """
    good_idxs = []
    for i in range(len(data) // 2):
        l_idx = i * 2
        if compare(data[l_idx], data[l_idx + 1]) < 0:
            good_idxs.append(i + 1)

    print(sum(good_idxs))

    """
    Part 2:
    Sort all lists from least to greatest after adding the two dividers
    Find index of the two dividers and return their product
    """
    # divider start and end
    div_s = [[2]]
    div_e = [[6]]

    data += [div_s, div_e]
    # TODO: Rewrite compare() to not require cmp_to_key()
    data = sorted(data, key=cmp_to_key(compare))

    start = 0
    end = 0
    for idx, val in enumerate(data):
        if val == div_s:
            start = idx + 1
        elif val == div_e:
            end = idx + 1

    print(start * end)

def compare(left, right):
    """
    +: right < left
    -: left < right
    0: equal
    """
    # standardize everything to list
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]

    # compare each element of list until a list runs out of values
    # or return statement becomes true
    for l_val, r_val in zip(left, right):
        if isinstance(l_val, list) or isinstance(r_val, list):
            result = compare(l_val, r_val)
        else:
            result = l_val - r_val
        if result:
            return result

    return len(left) - len(right)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

