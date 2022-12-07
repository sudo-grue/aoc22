#!/usr/bin/env python3


def main():
    data = []
    with open("input.txt", "r") as file:
        data = file.readlines()

    stack = []
    totals = []
    for line in data:
        # if doing directory traversal
        if line.startswith("$ cd"):
            # if cd forward
            if not line.endswith("..\n"):
                # set 0 as current dir size
                stack.append(0)
            # finished current dir (cd ..)
            else:
                # pop off the current (deepest) dir
                single = stack.pop()
                # add total to parent dir
                stack[-1] += single
                # add dir size to totals list
                totals.append(single)
        # file size found
        elif line[0].isdigit():
            # add size to current dir
            stack[-1] += int(line.split()[0])

    # collapse remaining dirs back to root
    while stack:
        single = stack.pop()
        # avoid idx error for root
        if stack:
            stack[-1] += single
        totals.append(single)

    # part1 filter to values less than limit and add together
    print(sum(val for val in totals if val < 100000))
    # part2 find smallest value that makes root size less than 40mil (allowing 30mil space)
    print(min(val for val in totals if totals[-1] - val <= 40000000))


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

