#!/usr/bin/env python3
"""
Monkies stole your stuff
Each monkey has specific rules of behavior
Line 1: Monkey ID (i.e. 0 thru 7)
Line 2: Items monkey currently possess (represented as ints)
Line 3: - Monkies assess each item, the specified math operator occurs to item
        - immediatly following previous math, the value is floor'd by 3 (//3)
Line 4: Evaluate each item with modulo defined, and apply to line 5 or 6
Line 5: If line 4 evaluates to true... pass item to that monkey
Line 6: If line 5 evaluates to false... pass item to other monkey
Line 7: --- BLANK ---

Evaluate the number items thrown by each monkey at 20 days and
provide the resulting sum of the top two throwers
"""

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
        self.items[0] = self._eval(self.items[0]) // 3
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

    
    for day in range(20):
        for idx, monkey in enumerate(monkeys):
            while monkey.items:
                monkey.eval
                item, tgt = monkey.test
                monkeys[tgt].catch(item)

    # TODO: Write function to return sum of max2
    for monkey in monkeys:
        print(monkey.rx)

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

