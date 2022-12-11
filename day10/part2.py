#!/usr/bin/env python3


def main():
    """
    CRT Display scheduling
    X value in register
    Cycle represents pixle position

    when range x to x+2 overlaps with current cycle value,
    print '#', else print '.'
    print a newline every 40 cycles
    the answer will be displayed in the ASCII art
    """
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
    
        sprite = set([x, x + 1, x + 2])
    
        if cycle in sprite:
            print("#", end="")
        else:
            print(".", end="")

        if 0 == cycle % 40:
            cycle = 0
            print()

        x += val


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

