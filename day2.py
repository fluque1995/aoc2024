def read_input():
    chains = []
    with open("inputs/day2.txt", "r") as fin:
        for line in fin:
            chains.append(list(map(int, line.strip().split())))

    return chains


def part1():
    chains = read_input()
    acc = 0
    for chain in chains:
        acc += 1 if (
            all([0 < i - j < 4 for i, j in zip(chain, chain[1:])])
            or all([0 > i - j > -4 for i, j in zip(chain, chain[1:])])
        ) else 0

    return acc


def part2():
    chains = read_input()
    acc = 0
    for chain in chains:
        for i in range(len(chain)):
            fixed_chain = chain[:i] + chain[i+1:]
            if (all([0 < i - j < 4 for i, j in zip(fixed_chain, fixed_chain[1:])])
                or all([0 > i - j > -4 for i, j in zip(fixed_chain, fixed_chain[1:])])):
                acc += 1
                break

    return acc


if __name__ == '__main__':
    print(part1())
    print(part2())
