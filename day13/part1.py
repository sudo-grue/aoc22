#!/usr/bin/env python3
"""
"""

import json

def main():
    data = []
    with open("input.txt", "r") as file:
        data = [json.loads(line.strip()) for line in file if line != '\n']

    proper = []
    for i in range(0, len(data), 2):
        if compare(data[i], data[i + 1]) < 0:
            proper.append(i // 2 + 1)

    print(sum(proper))

def compare(left, right):
    #print(f"    Compare {left} vs {right}")
    l_ans = isinstance(left, int)
    r_ans = isinstance(right, int)

    """
    + means right < left
    - means left < right
    0 means equal
    """
    if l_ans and r_ans:
        return left - right
    elif not l_ans and not r_ans:
        l_len = len(left)
        r_len = len(right)
        shortest = l_len if l_len < r_len else r_len

        for i in range(shortest):
            result = compare(left[i], right[i])
            if result:
                return result
        return l_len - r_len

    if l_ans:
        left = [left]
    elif r_ans:
        right = [right]

    return compare(left, right)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

