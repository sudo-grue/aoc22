#!/usr/bin/env python3
from sys import argv
from traceback import print_exc


def main():
    hands = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    part1 = 0
    part2 = 0

    with open("input.txt", "r") as file:
        for line in file:
            # part1: Am I one "index" ahead of opponent
            opp, me = line.split()
            if (hands[opp] + 1) % 3 == hands[me]:
                part1 += 6
            elif hands[opp] == hands[me]:
                part1 += 3
            # else we lost += 0
            # convert score back to 1's indexing
            part1 += hands[me] + 1

            # set mod back to default
            mod = 2
            # set conditions for tie
            if 'Y' == me:
                part2 += 3
                mod = 0
            # set conditions for win
            elif 'Z' == me:
                part2 += 6
                mod = 1

            # convert remainder of score back to ones indexing
            part2 += (hands[opp] + mod) % 3 + 1


    print(f"{part1 = }\t{part2 = }")


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print_exc()

