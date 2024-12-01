def read_input() -> tuple[list[int], list[int]]:
    lhs_input, rhs_input = [], []
    with open("inputs/day1.txt", "r") as fin:
        for line in fin:
            lhs, rhs = line.strip().split()
            lhs_input.append(int(lhs))
            rhs_input.append(int(rhs))
    return lhs_input, rhs_input


def part1():
    lhs, rhs = read_input()
    return sum(map(lambda x, y: abs(x - y), sorted(lhs), sorted(rhs)))


def part2():
    lhs, rhs = read_input()
    already_processed = []
    acc = 0
    for elem in lhs:
        if elem in already_processed:
            continue
        acc += (
            elem
            * len([i for i in lhs if i == elem])
            * len([i for i in rhs if i == elem])
        )
    return acc


if __name__ == '__main__':
    print(part1())
    print(part2())
