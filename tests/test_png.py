import tempfile

import png

from pretty_poly.png import write_colored_blocks_png, write_lines_png

from examples.right_12 import TILING as RIGHT_12


def test_basic_png_right_size():
    tiling = [[(0, 1), (0, 0)], [(1, 1), (1, 0)]]
    f, filename = tempfile.mkstemp(suffix=".png")
    write_colored_blocks_png(filename, tiling)
    r = png.Reader(filename)
    width, height, rows, info = r.read()
    assert width == 20
    assert height == 20


def test_large_nonrectangular_tiling():
    f, filename = tempfile.mkstemp(suffix=".png")
    write_colored_blocks_png(filename, RIGHT_12)
    r = png.Reader(filename)
    width, height, rows, info = r.read()
    assert rows is not None
    assert info is not None


def test_thick_lines_and_margins():
    f, filename = tempfile.mkstemp(suffix=".png")
    size, thickness = 10, 3
    expected_width = 4 * size + 3 * thickness
    expected_height = 4 * size + 3 * thickness
    tiles = [[(0, 0), (0, 1), (1, 0)], [(1, 1)]]
    write_lines_png(filename, tiles, size, thickness)
    r = png.Reader(filename)
    width, height, rows, info = r.read()
    assert width == expected_width
    assert height == expected_height
