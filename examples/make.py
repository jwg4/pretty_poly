from pretty_poly.png import write_colored_blocks_png, write_lines_png

from .right_12 import TILING as RIGHT_12


def write_examples():
    write_lines_png("examples/lines.png", [[(0, 0), (0, 1), (1, 0)], [(1, 1)]])
    write_colored_blocks_png("examples/right_12.png", RIGHT_12)
