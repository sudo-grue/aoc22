#!/usr/bin/env python3
from sys import argv
from traceback import print_exc


def get_elf_cals(raw_data):
    elf = []
    for entry in raw_data:
        if entry == '\n':
            yield elf
            elf = []
        else:
            elf.append(int(entry))

def main():
    with open("input.txt", "r") as file:
        elves = [sum(pack) for pack in get_elf_cals(file.readlines())]
        elves = sorted(elves, reverse=True)

    print(f"sum({elves[:3]}) = {sum(elves[:3])}")


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print_exc()

