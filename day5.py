from collections import defaultdict
from functools import cmp_to_key


def read_input():

    with open("inputs/day5.txt", "r") as fin:
        orders, manuals = fin.read().split("\n\n")

    orders = list(map(lambda x: list(map(int, x.split("|"))), orders.split("\n")))
    manuals = list(map(lambda x: list(map(int, x.split(","))), manuals.strip().split("\n")))
    biggers = defaultdict(list)
    for lhs, rhs in orders:
        biggers[lhs].append(rhs)


    return biggers, manuals


def part1():
    biggers, manuals = read_input()
    acc = 0
    for manual in manuals:
        valid = True
        for i, elem in enumerate(manual):
            if any([prev in biggers[elem] for prev in manual[:i]]):
                valid = False
                break

        if valid:
            acc += manual[len(manual) // 2]

    return acc


def part2():
    biggers, manuals = read_input()
    acc = 0

    for manual in manuals:
        valid = True
        for i, elem in enumerate(manual):
            if any([prev in biggers[elem] for prev in manual[:i]]):
                valid = False
                break

        if not valid:
            ordered = sorted(manual, key=cmp_to_key(lambda x, y: -1 if y in biggers[x] else 1))
            acc += ordered[len(ordered) // 2]

    return acc


if __name__ == '__main__':
    print(part1())
    print(part2())
