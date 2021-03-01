import random

import png

from .abstract import make_design


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def make_png(tiling, scale=10):
    grid, _, _, _ = make_design(tiling)
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
    return writer


def write_png(filename, tiling, scale=10):
    writer = make_png(tiling)
    with open(filename, 'w') as f:
        writer.write(f, color_data)
