#!/usr/bin/env python3

import re
from collections import Counter

#filename = "sample.txt"
filename = "input.txt"
limits = 20

def main():
    global limits
    if filename == "input.txt":
        limits = 4000000

    points = []
    with open(filename, "r") as file:
        for line in file:
            result = list(map(int, re.findall("-?\d+", line)))
            dist = manhatten(*result)
            result.append(dist)
            points.append(result)

    possibles = get_intersections(points)
    for x, y in possibles:
        if inrange((x, y), points):
            print(f"Answer: ({x}, {y}) = {4000000 * x + y}")
            break


def get_intersections(points):
    crossing = {}
    for point in points:
        sx, sy, bx, by, dist = point
        for x in range(sx - dist, sx + dist + 1):
            # increase to be +1 outside of range
            offset = dist - abs(sx - x) + 1
            min_y = sy - offset
            max_y = sy + offset
            # attempt to keep dataset small
            if (0 <= x <= limits) and (0 <= min_y <= limits):
                crossing[(x, min_y)] = crossing.get((x, min_y), 0) + 1
            if (0 <= x <= limits) and (0 <= max_y <= limits):
                crossing[(x, max_y)] = crossing.get((x, max_y), 0) + 1
            length = len(crossing)

    return (k for k, v in crossing.items() if 1 < v)

def inrange(target, points):
    x, y = target
    for point in points:
        sx, sy, bx, by, dist = point
        offset = dist - abs(sx - x)
        if (sx - dist - 1) < x < (sx + dist + 1):
            if (sy - offset - 1) < y < (sy + offset + 1):
                return False
    return True

def manhatten(sx, sy, bx, by):
    return abs(sx - bx) + abs(sy - by)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

