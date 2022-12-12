#!/usr/bin/env python3
"""
Same as part 1, except find shortest path from all 'a' values and
return distance of best one
"""
from time import time

def main():
    start = None
    end = None
    matrix = []
    starts = []
    with open("input.txt", "r") as file:
        for x, line in enumerate(file):
            matrix.append([])
            for y, letter in enumerate(line.strip()):
                if letter == "S":
                    matrix[-1].append("a")
                    start = (x, y)
                    starts.append(start)
                elif letter == "E":
                    matrix[-1].append("z")
                    end = (x, y)
                elif letter == 'a':
                    starts.append((x, y))
                    matrix[-1].append(letter)
                else:
                    matrix[-1].append(letter)

    paths = [bfs(matrix, point, end) for point in starts]
    # remove None objects from failed searches
    lens = [len(path) for path in paths if path is not None]

    # -1 for start point
    print(min(lens) - 1)

def bfs(matrix, start, end):
    # so it doesn't look like it's frozen
    print(f"BFS Origin: {start}")
    frontier = [[start]]
    explored = []

    if start == end:
        return [start]

    counter = 0

    while frontier:
        path = frontier.pop(0)
        node = path[-1]
        if node not in explored:

            for neighbor in get_neighbors(matrix, node):
                new_path = path.copy()
                new_path.append(neighbor)
                frontier.append(new_path)

                if neighbor == end:
                    return new_path

        explored.append(node)
    return None


def get_neighbors(matrix, node):
    x_min = 0
    y_min = 0
    x_max = len(matrix) - 1
    y_max = len(matrix[0]) - 1
    x, y = node

    # +2 to allow cap compmarison of 1 step above
    node_height = ord(matrix[x][y]) + 2

    neighbors = []
    # ensure X isn't an edge and left isn't taller than + 1
    if (x_min < x) and (ord(matrix[x - 1][y]) < node_height):
        neighbors.append((x - 1, y))

    # same for right
    if (x < x_max) and (ord(matrix[x + 1][y]) < node_height):
        neighbors.append((x + 1, y))

    # same for top
    if (y_min < y) and (ord(matrix[x][y - 1]) < node_height):
        neighbors.append((x, y - 1))

    # same for bottom
    if (y < y_max) and (ord(matrix[x][y + 1]) < node_height):
        neighbors.append((x, y + 1))

    return neighbors


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

