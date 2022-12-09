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
    head = Rope()
    one = Rope()
    two = Rope()
    three = Rope()
    four = Rope()
    five = Rope()
    six = Rope()
    seven = Rope()
    eight = Rope()
    tail = Rope()

    with open("input.txt", "r") as file:
        for line in file:
            act, times = line.split()
            for _ in range(int(times)):
                head.move(act)
                one.follow(head)
                two.follow(one)
                three.follow(two)
                four.follow(three)
                five.follow(four)
                six.follow(five)
                seven.follow(six)
                eight.follow(seven)
                tail.follow(eight)

    print(len(tail.been))


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

