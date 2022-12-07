#!/usr/bin/env python3


def main():
    sizes = []
    totals = []
    data = open("input.txt", "r").readlines()
    for line in data:
        if line.startswith("$ cd"):
            data = line.split()[2]
            if data != "..":
                sizes.append(0)
            else:
                output = sizes.pop()
                sizes[-1] += output
                totals.append(output)

        elif line[0].isdigit():
            sizes[-1] += int(line.split()[0])

    while 1 < len(sizes):
        output = sizes.pop()
        sizes[-1] += output

    empty = 70000000 - sizes[0]
    enough = []
    for size in totals:
        if 30000000 <= (empty + size):
            enough.append(size)

    print(min(enough))


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

