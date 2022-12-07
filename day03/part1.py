#!/usr/bin/env python3


def main():
    file = open("input.txt", "r")
    total = 0

    for line in file:
        length = len(line.strip())
        # create set for first half
        a = set(line[:length//2])
        # create set for second half
        b = set(line[length//2:])

        # find intersection between sets (commonality)
        result = list(a.intersection(b))[0]

        # convert character to 1's index of ascii
        total += ord(result) % 32
        if not result.islower():
            # add 26 for uppercase
            total += 26

    file.close()
    print(total)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

