import random
import re

import png


def print_alpha_blocks(grid):
    chars = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    table = [[chars[n] for n in l] for l in grid]
    for row in table:
        print "".join(row)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def create_png(grid, scale=10):
    d = dict()
    color_data = []
    palette = []
    for r in grid:
        out_row = []
        for c in r:
            if c not in d:
                d[c] = random_color()
            for i in range(scale):
                out_row.append(len(palette))
            palette.append(d[c])
        for i in range(scale):
            color_data.append(out_row)
    height = len(grid) * scale
    width = len(grid[0]) * scale
    writer = png.Writer(width=width, height=height, palette=palette)
    with open("output.png", "w") as f:
        writer.write(f, color_data)


def create_line_png(grid, scale=10):
    height = len(grid) * scale + 1
    width = len(grid[0]) * scale + 1
    palette = [(255, 255, 255), (0, 0, 0)]
    data = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        data[i][0] = 1
        data[i][width - 1] = 1
    for i in range(width):
        data[0][i] = 1
        data[height - 1][i] = 1
    for j in range(len(grid)):
        for i in range(len(grid[j]) - 1):
            if grid[j][i] != grid[j][i + 1]:
                for k in range(scale + 1):
                    data[(i + 1) * scale][j * scale + k] = 1
    for j in range(len(grid) - 1):
        for i in range(len(grid[j])):
            if grid[j][i] != grid[j + 1][i]:
                for k in range(scale + 1):
                    data[i * scale + k][(j + 1) * scale] = 1
    writer = png.Writer(width=width, height=height, palette=palette)
    with open("lines.png", "w") as f:
        writer.write(f, data)


count = 1

f = open("13x13-result", "r")

table = [([" "] * 13) for i in range(13)]

for l in f.readlines():
    m = re.match(r"square (\d+) (\d+) monomino (\d+)", l)
    if m:
        row = int(m.group(1))
        column = int(m.group(2))
        table[row][column] = count
        count = count + 1
    m = re.match(
        r"square (\d+) (\d+) square (\d+) (\d+) square (\d+) (\d+) square (\d+) (\d+)",
        l,
    )
    if m:
        for j in range(4):
            row = int(m.group(2 * j + 1))
            column = int(m.group(2 * j + 2))
            table[row][column] = count
        count = count + 1

print_alpha_blocks(table)
create_png(table)
create_line_png(table)
