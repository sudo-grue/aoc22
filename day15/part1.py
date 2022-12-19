#!/usr/bin/env python3

import re

#filename = "sample.txt"
filename = "input.txt"
target = 10

def main():
    global target
    if filename == "input.txt":
        target = 2000000

    data = []
    sensors = set()
    beacons = set()
    with open("input.txt", "r") as file:
        for line in file:
            points = list(map(int, re.findall("-?\d+", line)))
            if points[1] == target:
                sensors.add(tuple(points[:1]))
            if points[3] == target:
                beacons.add(tuple(points[2:]))
            data.append(inrange(*points))

    impossible = set()
    for beacon in data:
        for coverage in beacon:
            if coverage[1] == target:
                impossible.add(coverage)

    print(len(impossible - sensors - beacons))


def inrange(sx, sy, dx, dy):
    dist = manhatten(sx, sy, dx, dy)

    area = set()
    # my original solution but python crashed with message "Killed"
    """
    for x in range(sx - dist, sx + dist + 1):
        offset = dist - abs(sx - x)
        for y in range(sy - offset, sy + offset + 1):
            if target == y:
                area.add((x, y))
    """
    # modification to ONLY calculate for target row 
    offset = dist - abs(sy - target)
    for x in range(sx - offset, sx + offset + 1):
        area.add((x, target))

    return area


def manhatten(sx, sy, bx, by):
    return abs(sx - bx) + abs(sy - by)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

