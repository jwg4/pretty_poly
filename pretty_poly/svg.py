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
