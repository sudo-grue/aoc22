#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy

def load_data(file):
    """
    for start of file, interpret visual starting stack into dictionary
    """
    db = defaultdict(list)
    for line in file:
        if line == "\n":
            break
        for i in range(9):
            idx = 4 * i
            if line[idx + 1].isalpha() and line[idx] == '[':
                db[str(i + 1)].append(line[idx + 1])

    # reverse stack since we read from top to bottom and top should
    # be first values exposed in stack
    for key in db:
        db[key].reverse()

    return db

def print_data(db):
    """
    To print in proper order since creation of db wasn't 1-9 order
    """
    for key in range(1, 10):
        print(db[str(key)][-1], end='')
    print()


def main():
    with open("input.txt", "r") as file:
        stacks = load_data(file)
        # copy would not duplicate internal lists, just the dictionary
        multi_stacks = deepcopy(stacks)

       # starts after newline gap left by load_data()
       for line in file:
            _, amt, _, src, _, dst = line.strip().split()
            amt = int(amt)
            loader = []
            # for however many boxes are supposed to be moved
            while amt:
                # take from source and put in destination
                stacks[dst].append(stacks[src].pop())
                # part2: put in a queue
                loader.append(multi_stacks[src].pop())
                amt -= 1

            # part2: empty queue
            while loader:
                multi_stacks[dst].append(loader.pop())


    print_data(stacks)
    print_data(multi_stacks)

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

