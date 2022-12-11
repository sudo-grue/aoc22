#!/usr/bin/env python3

class Monkey():
    def __init__(self, items):
        self.items = items
        self.rx = 0
        self._eval = None
        self._test = None
        self._true = None
        self._false = None

    @property
    def eval(self):
        # TODO: Write function to apply LCM to all monkeys
        self.items[0] = self._eval(self.items[0]) % 9699690
        self.rx += 1
        return self.items[0]

    @eval.setter
    def eval(self, formula):
        self._eval = lambda old: eval(formula)

    @property
    def test(self):
        result = self.items[0] % self._test == 0
        val = self.items.pop(0)
        return (val, self.true) if result else (val, self.false)

    @test.setter
    def test(self, modulo):
        self._test = modulo

    @property
    def true(self):
        return self._true

    @true.setter
    def true(self, target):
        self._true = target

    @property
    def false(self):
        return self._false

    @false.setter
    def false(self, target):
        self._false = target

    @property
    def catches(self):
        return self.rx

    def catch(self, item):
        self.items.append(item)


def main():
    file = open("input.txt", "r")
    data = file.readlines()
    monkeys = []
    for idx in range(0, len(data), 7):
        _, items = data[idx + 1].split(": ")
        items = [int(item) for item in items.split(", ")]
        monkey = Monkey(items)
        monkey.eval = data[idx + 2].split("= ")[1].strip()
        monkey.test = int(data[idx + 3].split("by ")[1])
        monkey.true = int(data[idx + 4].split("monkey ")[1])
        monkey.false = int(data[idx + 5].split("monkey ")[1])

        monkeys.append(monkey)
    file.close()

    
    for day in range(1, 10001):
        for monkey in monkeys:
            while monkey.items:
                monkey.eval
                item, tgt = monkey.test
                monkeys[tgt].catch(item)
        if 0 == day % 1000:
            print(f"--- Day {day} ---")


    # TODO: Write function to return product of max2
    for monkey in monkeys:
        print(monkey.rx)
    print()

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

