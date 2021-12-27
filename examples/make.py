import os

from pretty_poly.png import write_colored_blocks_png, write_lines_png
from pretty_poly.svg import write_colored_blocks_svg, write_lines_svg

from .right_12 import TILING as RIGHT_12


def write_examples():
    directory = "examples/images"
    if not os.path.exists(directory):
        os.makedirs(directory)

    write_lines_png("examples/images/lines.png", [[(0, 0), (0, 1), (1, 0)], [(1, 1)]])
    write_lines_svg("examples/images/lines.svg", [[(0, 0), (0, 1), (1, 0)], [(1, 1)]])
    write_lines_png("examples/images/thick.png", RIGHT_12, 10, 3)
    write_lines_svg("examples/images/thick.svg", RIGHT_12, 10, 3)
    write_colored_blocks_png("examples/images/right_12.png", RIGHT_12)
    write_colored_blocks_svg("examples/images/right_12.svg", RIGHT_12)
