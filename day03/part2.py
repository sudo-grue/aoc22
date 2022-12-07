#!/usr/bin/env python3


def main():
    file = open("input.txt", "r")
    total = 0
    idx = 0

    # read entire file at once to allow for handling multi-line task
    data = file.readlines()
    length = len(data)

    while idx < length:
        # establish set for each 3 lines
        a = set(data[idx].strip())
        b = set(data[idx + 1].strip())
        c = set(data[idx + 2].strip())

        # find intersecting character of all 3 lines
        result = list(a.intersection(b.intersection(c)))[0]

        # convert to 1's index ascii
        total += ord(result) % 32
        if not result.islower():
            # add 26 for uppercase
            total += 26

        idx += 3

    file.close()
    print(total)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

