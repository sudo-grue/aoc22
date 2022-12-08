#!/usr/bin/env python3


def main():
    matrix = []
    with open("input.txt", "r") as file:
        for idx, line in enumerate(file):
            matrix.append([])
            for val in line.strip():
                matrix[idx].append(int(val))

    best_score = 0
    best_pos = ()
    # run is_visible from all trees
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            score = has_sight(matrix, row, col)
            if best_score < score:
                best_score = score
                best_pos = (row, col)

    print(f"{best_pos = } {best_score = }")
    has_sight(matrix, 29, 49)


def has_sight(matrix, x, y):
    # current tree's height
    current = matrix[x][y]
    scores = [0, 0, 0, 0]

    for idx in range(y - 1, -1, -1):
        scores[0] += 1
        if current <= matrix[x][idx]:
            break

    east = 0
    for idx in range(y + 1, len(matrix[0])):
        scores[1] += 1
        if current <= matrix[x][idx]:
            break

    north = 0
    for idx in range(x - 1, -1, -1):
        scores[2] += 1
        if current <= matrix[idx][y]:
            break

    south = 0
    for idx in range(x + 1, len(matrix)):
        scores[3] += 1
        if current <= matrix[idx][y]:
            break

    for idx in range(len(scores)):
        if scores[idx] == 0:
            scores[idx] = 1

    return scores[0] * scores[1] * scores[2] * scores[3]


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

