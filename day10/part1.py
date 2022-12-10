#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as file:
        queue = []
        for line in file:
            line = line.split()
            if len(line) == 2:
                queue.append([int(line[1]), 1])
            else:
                queue.append([0, 0])

    totals = []
    x = 1
    cycle = 0
    while queue:
        val = 0
        if queue[0][1]:
            queue[0][1] -= 1
        else:
            val, _ = queue.pop(0)

        cycle += 1

        if 20 == cycle % 40:
            totals.append(cycle * x)

        x += val


    print(sum(totals))




if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

