import itertools

def parse_input():
    charmap = []
    with open("inputs/day4.txt", "r") as fin:
        for line in fin:
            charmap.append(line.strip())

    return charmap


def check_starting_position(charmap, i, j, imax, jmax, string):
    acc = 0
    for drows, dcols in itertools.product((-1, 0, 1), (-1, 0, 1)):
        for k in range(4):
            curr_i = i + drows * k
            curr_j = j + dcols * k
            if  not (0 <= curr_i < imax and 0 <= curr_j < jmax) or charmap[curr_i][curr_j] != string[k]:
                break
        else:
            acc += 1

    return acc


def part1():
    charmap = parse_input()
    acc = 0
    imax, jmax = len(charmap[0]), len(charmap)
    for i in range(imax):
        for j in range(jmax):
            acc += check_starting_position(charmap, i, j, imax, jmax, "XMAS")

    return acc


def part2():
    charmap = parse_input()
    acc = 0
    for i in range(1, len(charmap[0]) - 1):
        for j in range(1, len(charmap) - 1):
            if (
                    charmap[i][j] == 'A'
                    and {charmap[i-1][j-1], charmap[i+1][j+1]} == {'M', 'S'}
                    and {charmap[i-1][j+1], charmap[i+1][j-1]} == {'M', 'S'}
            ):
                acc += 1

    return acc


if __name__ == '__main__':
    print(part1())
    print(part2())
