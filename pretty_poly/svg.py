import svgwrite

from .image import make_colored_blocks, make_lines, make_blocks_and_lines
from .abstract import make_design


def svg_color(rgb):
    """
    >>> from pretty_poly.svg import svg_color
    >>> svg_color((123, 234, 45))
    'rgb(123, 234, 45)'

    """
    return "rgb(%d, %d, %d)" % rgb


def write_colored_blocks_svg(filename, tiling, scale=10):
    faces, _, _, _ = make_design(tiling)
    data, palette = make_colored_blocks(tiling, scale)
    size = len(data[0]), len(data)
    dwg = svgwrite.Drawing(filename, size=size)
    for y, row in enumerate(faces):
        for x, sq in enumerate(row):
            if sq < 0:
                continue
            color = svg_color(palette[sq])
            square = dwg.rect((x * scale, y * scale), (scale, scale), fill=color)
            dwg.add(square)

    dwg.save()


def write_lines_svg(filename, tiling, scale=10, width=1):
    faces, vertical, horizontal, nodes = make_design(tiling)
    data, palette = make_lines(tiling, scale, width)
    size = len(data[0]), len(data)
    dwg = svgwrite.Drawing(filename, size=size)
    for i, row in enumerate(vertical):
        for j, value in enumerate(row):
            if value:
                x = j * scale
                y = i * scale + width
                color = svg_color(palette[1])
                vline = dwg.rect(
                    (x, y), (width, scale - width), fill=color
                )
                dwg.add(vline)
    for i, row in enumerate(horizontal):
        for j, value in enumerate(row):
            if value:
                x = j * scale + width
                y = i * scale
                color = svg_color(palette[1])
                hline = dwg.rect(
                    (x, y), (scale - width, width), fill=color
                )
                dwg.add(hline)
    for i, row in enumerate(nodes):
        for j, value in enumerate(row):
            if value:
                x = j * scale
                y = i * scale
                color = svg_color(palette[1])
                hline = dwg.rect(
                    (x, y), (width, width), fill=color
                )
                dwg.add(hline)

    dwg.save()
