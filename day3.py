import re

def read_input():
    with open("inputs/day3.txt", "r") as fin:
        return fin.read().rstrip()


def day1():
    line = read_input()
    regex = re.compile(r"mul\(\d\d?\d?,\d\d?\d?\)")
    filtered = regex.findall(line)

    acc = 0
    for prod in filtered:
        lhs, rhs = map(int, prod[4:-1].split(","))
        acc += lhs * rhs

    return acc


def day2():
    line = read_input()
    regex = re.compile(r"mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)")
    filtered = regex.findall(line)

    acc = 0
    active = True
    for prod in filtered:
        if prod == "do()":
            active = True
        elif prod == "don't()":
            active = False
        elif active:
            lhs, rhs = map(int, prod[4:-1].split(","))
            acc += lhs * rhs

    return acc


if __name__ == '__main__':
    print(day1())
    print(day2())
    
