#!/usr/bin/env python3


def main():
    file = open("input.txt", "r")
    total = 0

    for line in file:
        length = len(line.strip())
        a = set(line[:length//2])
        b = set(line[length//2:])

        result = list(a.intersection(b))[0]

        total += ord(result) % 32
        if not result.islower():
            total += 26

    file.close()
    print(total)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

