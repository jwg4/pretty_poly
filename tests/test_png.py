import tempfile

import png

from pretty_poly.png import write_colored_blocks_png


def test_basic_png_right_size():
    tiling = [
        [(0, 1), (0, 0)],
        [(1, 1), (1, 0)]
    ]
    f, filename = tempfile.mkstemp(suffix=".png")
    write_colored_blocks_png(filename, tiling)
    r = png.Reader(filename)
    width, height, rows, info = r.read()
    assert width == 20
    assert height == 20
    
