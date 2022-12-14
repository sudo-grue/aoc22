#!/usr/bin/env python3


def main():
    matrix = []
    with open("input.txt", "r") as file:
        for idx, line in enumerate(file):
            matrix.append([int(val) for val in line.strip()])

    seen = 0
    # run is_visible from all trees
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_visible(matrix, row, col):
                seen += 1

    print(f"{seen = }")

def is_visible(matrix, x, y):
    # default handling for all "edge" cases lol
    if x == 0 or y == 0 or x == (len(matrix) - 1) or y == (len(matrix[0]) - 1):
            return True

    # current tree's height
    current = matrix[x][y]
    # if all west
    if all((val < current for val in matrix[x][:y])):
        return True
    # if all east
    if all((val < current for val in matrix[x][y + 1:])):
        return True
    # if all north
    if all((matrix[idx][y] < current for idx in range(x))):
        return True
    # if all south
    if all((matrix[idx][y] < current for idx in range(x + 1, len(matrix)))):
        return True

    return False

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

