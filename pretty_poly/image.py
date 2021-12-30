import random

from .abstract import make_design


def random_color():
    r,g,b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if max(r, g, b) < 20:
        return random_color()
    return r, g, b


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
    faces, vertical, horizontal, nodes = make_design(tiling, False)
    x, y = len(faces[0]), len(faces)
    sx, sy = (x + 2) * scale - width, (y + 2) * scale - width
    color_data = [[0 for i in range(0, sx)] for j in range(0, sy)]
    palette = [(255, 255, 255), (0, 0, 0)]
    for i, row in enumerate(vertical):
        for j, value in enumerate(row):
            if value:
                for z in range(0, scale - width):
                    for w in range(0, width):
                        color_data[(i + 1) * scale + width - 1 + z][
                            (j + 1) * scale + w - 1
                        ] = 1
    for i, row in enumerate(horizontal):
        for j, value in enumerate(row):
            if value:
                for z in range(0, scale - width):
                    for w in range(0, width):
                        color_data[(i + 1) * scale + w - 1][
                            (j + 1) * scale + width - 1 + z
                        ] = 1
    for i, row in enumerate(nodes):
        for j, value in enumerate(row):
            color = 1 if value else 0
            for z in range(0, width):
                for w in range(0, width):
                    color_data[(i + 1) * scale + w - 1][(j + 1) * scale + z - 1] = color

    return color_data, palette


def make_blocks_and_lines(tiling, scale=10, width=1):
    return []
