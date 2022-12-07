#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as file:
        contain = 0
        overlap = 0
        for line in file:
            # extract first and second elf efforts
            first, second = line.strip().split(',')

            # use generator to create set of first elf efforts
            left, right = first.split('-')
            first = set(range(int(left), int(right) + 1))

            # use generator to create set for second elf efforts
            left, right = second.split('-')
            second = set(range(int(left), int(right) + 1))

            # part1: if either elf is a complete subset(superset) of the other
            if first.issubset(second) or second.issubset(first):
                contain += 1

            # part2: if there's any overlap in set
            if first.intersection(second):
                overlap += 1

    print(f"{contain = }\n{overlap = }")

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

