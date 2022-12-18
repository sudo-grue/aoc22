#!/usr/bin/env python3
"""
I realized conducting a SINGLE BFS from the endpoint and keeping
all level distance from endpoint is much more efficient than
running a BFS from every start point.
"""

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

    # conduct BFS from endpoint so all distances are labeled correctly
    # returns dictionary so can then iterate through "best" for part 2
    answers = bfs(matrix, end)

    # filter out impossible to discover points
    totals = [answers.get(point) for point in starts if answers.get(point)]

    print(answers[start])
    print(min(totals))

def bfs(matrix, end):
    frontier = [end]
    level = dict()
    level[end] = 0

    while frontier:
        current = frontier.pop(0)
        for neighbor in get_neighbors(matrix, current):
            if neighbor not in level:
                level[neighbor] = level[current] + 1
                frontier.append(neighbor)

    return level


def get_neighbors(matrix, node):
    x_min = 0
    y_min = 0
    x_max = len(matrix) - 1
    y_max = len(matrix[0]) - 1
    x, y = node

    # -2 allowing only single steps down the mountain
    node_height = ord(matrix[x][y]) - 2

    neighbors = []

    # ensure X isn't an edge and left isn't lower than - 1 height
    if (x_min < x) and (node_height < ord(matrix[x - 1][y])):
        neighbors.append((x - 1, y))

    # same for right
    if (x < x_max) and (node_height < ord(matrix[x + 1][y])):
        neighbors.append((x + 1, y))

    # same for top
    if (y_min < y) and (node_height < ord(matrix[x][y - 1])):
        neighbors.append((x, y - 1))

    # same for bottom
    if (y < y_max) and (node_height < ord(matrix[x][y + 1])):
        neighbors.append((x, y + 1))

    return neighbors


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

