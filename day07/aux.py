#!/usr/bin/env python3

def main():
    fs = []
    with open("input.txt", "r") as file:
        for line in file:
            if line.startswith("$ cd"):
                data = line.split()[2]
                if data != "..":
                    fs.append(f"{data}/")
                else:
                    fs.pop()
                print("".join(fs))


if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()


