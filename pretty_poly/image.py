import random

from .abstract import make_design


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def make_colored_blocks(tiling, scale=10):
    grid, _, _, _ = make_design(tiling, False)
    color_lookup = {-2: (0, 0, 0)}
    palette_lookup = {-2: 0}
    color_data = []
    palette = [(0, 0, 0)]
    for r in grid:
        out_row = []
        for c in r:
            if c not in color_lookup:
                color_lookup[c] = random_color()
                palette.append(color_lookup[c])
                palette_lookup[c] = len(palette)
            for i in range(scale):
                out_row.append(palette_lookup[c])
        for i in range(scale):
            color_data.append(out_row)
    return color_data, palette


def make_lines(tiling, scale=10, width=1):
    return []


def make_blocks_and_lines(tiling, scale=10, width=1):
    return []
