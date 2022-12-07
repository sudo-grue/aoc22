#!/usr/bin/env python3


def main():
    part1 = 0
    part2 = 0
    with open("input.txt", "r") as file:
        code = file.read().strip()

        for idx in range(len(code)):
            # slice and convert to set (dedup)
            chunk4 = set(code[idx:idx + 4])
            chunk14 = set(code[idx:idx + 14])

            # if set is proper length, we had no duplicates
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

