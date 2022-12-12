#!/usr/bin/env python3
"""
Climbing
2d matrix of heights, conduct BFS from S and end at E. Limitation, can only
move up or down one height difference (i.e. m->n but not m->o).

S will be represented by backtick because 96 == ord(`) and
E will be represented by open-curly because 123 = ord({)
allowing ascii characters to still function in the +/- 1 behavior required

Looks terribly inefficient but interesting idea for tracking backpath
https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/


Part 1:
Report how many steps from S to E.
"""

def main():
    start = None
    end = None
    matrix = []
    with open("input.txt", "r") as file:
        for x, line in enumerate(file):
            matrix.append([])
            for y, letter in enumerate(line.strip()):
                # standardize height for Start and End
                if letter == "S":
                    matrix[-1].append("a")
                    start = (x, y)
                elif letter == "E":
                    matrix[-1].append("z")
                    end = (x, y)
                else:
                    matrix[-1].append(letter)

    # -1 to remove starting point
    print(len(bfs(matrix, start, end)) - 1)


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end="")
        print()

def bfs(matrix, start, end):
    frontier = [[start]]
    explored = []

    if start == end:
        return [start]

    counter = 0

    while frontier:
        # pop pathlist
        path = frontier.pop(0)
        # get last seen node in current pathlist
        node = path[-1]
        # if we've never explored this node before, we have things to do
        if node not in explored:

            for neighbor in get_neighbors(matrix, node):
                # copy current path for each discovered node and queue back up
                new_path = path.copy()
                new_path.append(neighbor)
                frontier.append(new_path)

                if neighbor == end:
                    return new_path

        explored.append(node)


def get_neighbors(matrix, node):
    x_min = 0
    y_min = 0
    x_max = len(matrix) - 1
    y_max = len(matrix[0]) - 1
    # filter by height
    x, y = node
    node_height = ord(matrix[x][y])

    neighbors = []
    if (x_min < x) and (ord(matrix[x - 1][y]) < node_height + 2):
            neighbors.append((x - 1, y))

    if (x < x_max) and (ord(matrix[x + 1][y]) < node_height + 2):
            neighbors.append((x + 1, y))

    if y_min < y and ord(matrix[x][y - 1]) < node_height + 2:
            neighbors.append((x, y - 1))

    if y < y_max and ord(matrix[x][y + 1]) < node_height + 2:
            neighbors.append((x, y + 1))

    return neighbors


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

