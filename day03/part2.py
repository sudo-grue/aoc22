#!/usr/bin/env python3


def main():
    file = open("input.txt", "r")
    total = 0
    idx = 0

    data = file.readlines()
    length = len(data)

    while idx < length:
        a = set(data[idx].strip())
        b = set(data[idx + 1].strip())
        c = set(data[idx + 2].strip())

        result = list(a.intersection(b.intersection(c)))[0]

        total += ord(result) % 32
        if not result.islower():
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

