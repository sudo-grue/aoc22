#!/usr/bin/env python3

class Rope:
    db = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1),
          2: 1, -2: -1, 1: 1, -1: -1, 0: 0}

    def __init__(self):
        self.x = 0
        self.y = 0
        self.been = set()

    def move(self, act):
        x, y = self.db[act]
        self.x += x
        self.y += y

    def follow(self, other):
        x = other.x - self.x
        y = other.y - self.y

        if 2 == abs(x) or 2 == abs(y):
            self.x += self.db[x]
            self.y += self.db[y]

        self.been.add((self.x, self.y))


def main():
    """
    The head of a rope receives directions of movement, when head is more
    than 1 square away (including diagonal) from rest of rope, the rest of
    the rope must follow

    Part 1: Tail is the next segment of rope behind head and can never be more
    than +/- 2 squares in one direction and +/- 1 squares in the other.

    Part 2: Tail is the 10th segment and each segment must follow the previous
    one. This creates the possibility of up to +/- 2 in both/either cardinal
    directions. 

    Directions appear in format 2 part format where the
    first portion is U, D, L, R and second portion is number of
    squares to move in that direction.
    """
    head = Rope()
    part1 = Rope()
    two = Rope()
    three = Rope()
    four = Rope()
    five = Rope()
    six = Rope()
    seven = Rope()
    eight = Rope()
    part2 = Rope()

    with open("input.txt", "r") as file:
        for line in file:
            act, times = line.split()
            for _ in range(int(times)):
                head.move(act)
                part1.follow(head)
                two.follow(part1)
                three.follow(two)
                four.follow(three)
                five.follow(four)
                six.follow(five)
                seven.follow(six)
                eight.follow(seven)
                part2.follow(eight)

    print(f"{len(part1.been) = }")
    print(f"{len(part2.been) = }")


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

