#!/usr/bin/env python3


def main():
    sizes = []
    total = 0
    data = open("input.txt", "r").readlines()
    for line in data:
        if line.startswith("$ cd"):
            data = line.split()[2]
            if data != "..":
                sizes.append(0)
            else:
                output = sizes.pop()
                sizes[-1] += output
                if output <= 100000:
                    total += output

        elif line[0].isdigit():
            sizes[-1] += int(line.split()[0])

    while 1 < len(sizes):
        output = sizes.pop()
        sizes[-1] += output
        if output <= 100000:
            total += output

    print(total)




        




if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

