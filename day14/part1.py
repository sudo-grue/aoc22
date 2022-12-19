#!/usr/bin/env python3

from os import system
from time import sleep

floor = 0
x_min = 1000
x_max = 0

def main():
    global floor
    global x_min
    global x_max
    # probably oversized but guarenteed to hold every possible point
    graph = [['.'] * 1000 for _ in range(250)]
    with open("sample.txt", "r") as file:
        for line in file:
            prev = [0, 0]
            lines = line.strip().split(" -> ")
            for wall in lines:
                y = int(wall.split(',')[0])
                x = int(wall.split(',')[1])
                
                if floor < x:
                    floor = x
                if y < x_min:
                    x_min = y
                if x_max < y:
                    x_max = y

                if prev != [0, 0]:
                    x_diff = prev[0] - x
                    if x_diff:
                        inc = 1 if x_diff < 0 else -1
                        for val in range(prev[0], x + inc, inc):
                            graph[val][y] = "#"
                    else:
                        inc = 1 if prev[1] - y < 0 else -1
                        for val in range(prev[1], y + inc, inc):
                            graph[x][val] = "#"

                prev[0] = x
                prev[1] = y
    
    sand = [0, 500]
    tracker = set()
    while sand[0] < floor:
        sand = [0, 500]
        #print_graph(graph)
        while True:
            x = sand[0]
            y = sand[1]
            if graph[x + 1][y] == '.':
                pass
            elif graph[x + 1][y - 1] == '.':
                sand[1] = y - 1
            elif graph[x + 1][y + 1] == '.':
                sand[1] = y + 1
            else:
                graph[x][y] = 'o'
                tracker.add(tuple(sand))
                break

            sand[0] = x + 1
            if sand[0] == floor:
                break

    print(len(tracker))
                
def print_graph(graph):
    sleep(0.1)
    system("clear")
    for idx, line in enumerate(graph):
        print("".join(line[x_min - 10:x_max + 10]))
        if floor < idx:
            break
            

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()

