#!/usr/bin/env python3

import math

def main():
    matrix = []
    with open("input.txt", "r") as file:
        for idx, line in enumerate(file):
            matrix.append([])
            for val in line.strip():
                matrix[idx].append(int(val))

    trees_seen = 0
    best_view = 0

    # check from every tree
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_visible(matrix, row, col):
                trees_seen += 1

            view = has_sight(matrix, row, col)
            if best_view < view:
                best_view = view

    print(f"{trees_seen = }\n{best_view = }")


def is_visible(matrix, row, col):
    tgt = matrix[row][col]

    # create generators for each direction
    west = (val < tgt for val in matrix[row][:col])
    east = (val < tgt for val in matrix[row][col + 1:])
    north = (matrix[y][col] < tgt for y in range(row))
    south = (matrix[y][col] < tgt for y in range(row + 1, len(matrix)))

    # all evaluates to true only if all items in iterable are true
    result = False
    if all(west) or all(east) or all(north) or all(south):
        result = True

    return result


def has_sight(matrix, row, col):
    # current tree's height
    tgt = matrix[row][col]
    scores = [0, 0, 0, 0]

    # generators to produce proper indexing from target tree
    west = range(col - 1, -1, -1)
    east = range(col + 1, len(matrix[0]))
    north = range(row - 1, -1, -1)
    south = range(row + 1, len(matrix))

    for idx in west:
        scores[0] += 1
        if tgt <= matrix[row][idx]:
            break
    
    for idx in east:
        scores[1] += 1
        if tgt <= matrix[row][idx]:
            break

    for idx in north:
        scores[2] += 1
        if tgt <= matrix[idx][col]:
            break

    for idx in south:
        scores[3] += 1
        if tgt <= matrix[idx][col]:
            break

    # handle "edge" cases where value would be 0, set to 1 for multiplication
    scores = [val if val else 1 for val in scores]

    return math.prod(scores)


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

