from pretty_poly.image import make_colored_blocks

from examples.right_12 import TILING as RIGHT_12


def test_make_colored_blocks():
    tiling = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(1, 0), (2, 0), (2, 1), (3, 0)]
    ]
    color_data, palette = make_colored_blocks(tiling)
    assert len(color_data) == 30
    assert len(color_data[0]) == 40
    assert len(palette) == 3, str(palette)


def test_large_nonrectangular_tiling():
    color_data, palette = make_colored_blocks(RIGHT_12)
    assert len(color_data) == 140
    assert len(color_data[0]) == 130
    assert len(palette) == 43, str(palette)
    assert (0, 0, 0) in palette
