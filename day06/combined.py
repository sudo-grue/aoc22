#!/usr/bin/env python3


def main():
    part1 = 0
    part2 = 0
    with open("input.txt", "r") as file:
        code = file.read().strip()

        for idx, _ in enumerate(code):
            chunk4 = set(code[idx:idx + 4])
            chunk14 = set(code[idx:idx + 14])

            if not part1 and len(chunk4) == 4:
                part1 = idx + 4

            if len(chunk14) == 14:
                part2 = idx + 14
                break

    print(f"{part1 = }\n{part2 = }")

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()

