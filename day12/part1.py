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
        for line in file:
            matrix.append([])
            for letter in line.strip():
                if letter == "S":
                    matrix[-1].append("`")
                    start = (len(matrix) - 1, len(matrix[-1] - 1))
                elif letter == "E":
                    matrix[-1].append("{")
                    end = (len(matrix) - 1, len(matrix[-1] - 1))
                else:
                    matrix[-1].append(letter)


def bfs(matrix, start, end):
    frontier = []
    frontier.append(start)
    explored = set()

    while frontier:
        curr = frontier.pop(0)
        if curr in explored:
            continue
        if curr =

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

