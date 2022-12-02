#!/usr/bin/env python3
from sys import argv
from traceback import print_exc


def main():
    hands = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    score = 0

    with open("input.txt", "r") as file:
        for line in file:
            opp, me = line.split()
            if (hands[opp] + 1) % 3 == hands[me]:
                score += 6
            elif hands[opp] == hands[me]:
                score += 3
            # else we lost += 0

            score += hands[me] + 1

    print(score)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print_exc()

