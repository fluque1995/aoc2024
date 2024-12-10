from collections import defaultdict


def parse_input():
    antennas = defaultdict(list)
    with open("inputs/day8.txt", "r") as fin:
        antennas_map = [row.strip() for row in fin]

    for i, line in enumerate(antennas_map):
        for j, character in enumerate(line):
            if character != '.':
                antennas[character].append((i,j))

    return antennas, len(antennas_map), len(antennas_map[0])


def inside_bounds(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col


def part1():
    antennas, max_row, max_col = parse_input()
    antinodes = set()
    for antenna, positions in antennas.items():
        for i, (init_r, init_c) in enumerate(positions[:-1]):
            for (end_r, end_c) in positions[i+1:]:
                dr, dc = end_r - init_r, end_c - init_c
                curr_r, curr_c = init_r - dr, init_c - dc
                if inside_bounds(curr_r, curr_c, max_row, max_col):
                    antinodes.add((curr_r, curr_c))
                curr_r, curr_c = end_r + dr, end_c + dc
                if inside_bounds(curr_r, curr_c, max_row, max_col):
                    antinodes.add((curr_r, curr_c))
    return len(antinodes)


def part2():
    antennas, max_row, max_col = parse_input()
    antinodes = set()
    for antenna, positions in antennas.items():
        for i, (init_r, init_c) in enumerate(positions[:-1]):
            for (end_r, end_c) in positions[i+1:]:
                dr, dc = end_r - init_r, end_c - init_c
                curr_r, curr_c = init_r, init_c
                while inside_bounds(curr_r, curr_c, max_row, max_col):
                    antinodes.add((curr_r, curr_c))
                    curr_r -= dr
                    curr_c -= dc

                curr_r, curr_c = end_r, end_c
                while inside_bounds(curr_r, curr_c, max_row, max_col):
                    antinodes.add((curr_r, curr_c))
                    curr_r += dr
                    curr_c += dc

    return len(antinodes)


if __name__ == '__main__':
    print(part1())
    print(part2())
