#!/usr/bin/env python3
from sys import argv
from traceback import print_exc


def main():
    total = 0
    everyone = []
    with open("input.txt", "r") as file:
        for line in file:
            try:
                total += int(line)
            except ValueError:
                everyone.append(total)
                total = 0
    print(sum(sorted(everyone, reverse=True)[:3]))



if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print_exc()

