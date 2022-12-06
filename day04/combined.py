#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as file:
        contain = 0
        overlap = 0
        for line in file:
            first, second = line.strip().split(',')

            left, right = first.split('-')
            first = set(range(int(left), int(right) + 1))

            left, right = second.split('-')
            second = set(range(int(left), int(right) + 1))

            if first.issubset(second) or second.issubset(first):
                contain += 1

            if first.intersection(second):
                overlap += 1

    print(f"{contain = }\n{overlap = }")

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

