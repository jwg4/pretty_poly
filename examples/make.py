from pretty_poly.png import write_colored_blocks_png, write_lines_png


def write_examples():
    write_lines_png("examples/lines.png", [[(0, 0), (0, 1), (1, 0)], [(1, 1)]])
