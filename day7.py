def parse_input():
    lines = []
    with open("inputs/day7.txt", "r") as fin:
        for line in fin:
            value, remainder = line.strip().split(": ")
            value = int(value)
            remainder = list(map(lambda x: int(x.strip()), remainder.split()))
            lines.append((value, remainder))
    return lines


def guess_operations(value, acc, elements):
    if len(elements) == 0:
        return acc == value
    if acc <= value:
        return guess_operations(value, acc + elements[0], elements[1:]) or guess_operations(value, acc * elements[0], elements[1:])
    return False


def part1():
    inputs = parse_input()
    acc = 0
    for value, remainder in inputs:
        if guess_operations(value, 0, remainder):
            acc += value
    return acc


def guess_operations_with_concat(value, acc, elements):
    if len(elements) == 0:
        return acc == value
    if acc <= value:
        return (
            guess_operations_with_concat(value, acc + elements[0], elements[1:])
            or guess_operations_with_concat(value, acc * elements[0], elements[1:])
            or guess_operations_with_concat(value,  int(str(acc) + str(elements[0])), elements[1:])
        )
    return False


def part2():
    inputs = parse_input()
    acc = 0
    for value, remainder in inputs:
        if guess_operations_with_concat(value, 0, remainder):
            acc += value
    return acc


if __name__ == '__main__':
    print(part1())
    print(part2())
