from itertools import combinations
import math


def read_input(file):
    with open(file) as f:
        return [int(x) for x in f]


def solve(puzzle, n):
    for c in combinations(puzzle, n):
        if sum(c) != 2020:
            continue
        return math.prod(c)


answer_1 = solve(read_input("input_01.txt"), 2)
answer_2 = solve(read_input("input_01.txt"), 3)

print(f"Die Loesung 1: {answer_1} \nDie Loesung 2: {answer_2}")
