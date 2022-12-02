#!/usr/bin/env python3
from sys import argv
from traceback import print_exc


def main():
    hands = {"A": 0, "B": 1, "C": 2}
    score = 0

    with open("input.txt", "r") as file:
        for line in file:
            opp, me = line.split()
            mod = 2 # default for loss
            if me == 'Y':
                score += 3
                mod = 0
            elif me == 'Z':
                score += 6
                mod = 1

            score += (hands[opp] + mod) % 3 + 1

    print(score)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print_exc()

