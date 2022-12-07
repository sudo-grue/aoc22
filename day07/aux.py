#!/usr/bin/env python3

def main():
    total = 0
    with open("input.txt", "r") as file:
        for line in file:
            if line[0].isdigit():
                total += int(line.split()[0])

    print(total)

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()


