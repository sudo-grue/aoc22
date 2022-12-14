#!/usr/bin/env python3

from collections import defaultdict

def load_data(file):
    db = defaultdict(list)
    for line in file:
        if line == '\n':
            break
        for i in range(9):
            idx = 4 * i
            if line[idx + 1].isalpha() and line[idx] == '[':
                db[str(i + 1)].append(line[idx + 1])

    for key in db:
        db[key].reverse()

    return db

def print_data(db):
    for key in range(1, 10):
        print(db[str(key)][-1], end='')
    print()


def main():
    with open("input.txt", "r") as file:
        stacks = load_data(file)
        for line in file:
            _, amt, _, src, _, dst = line.strip().split()
            amt = int(amt)
            while amt:
                stacks[dst].append(stacks[src].pop())
                amt -= 1

    print_data(stacks)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

