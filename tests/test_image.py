from pretty_poly.image import make_colored_blocks, make_lines

from examples.right_12 import TILING as RIGHT_12


def test_make_colored_blocks():
    tiling = [[(0, 0), (0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (2, 1), (3, 0)]]
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


def test_make_black_lines():
    tiling = [[(0, 0), (0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (2, 1), (3, 0)]]
    color_data, palette = make_lines(tiling)
    assert len(color_data) == 51
    assert len(color_data[0]) == 61
    assert len(palette) == 2, str(palette)


def test_make_black_lines_with_thickness():
    size, thickness = 10, 3
    expected_width = 4 * size + thickness
    expected_height = 4 * size + thickness
    tiling = [[(0, 0), (0, 1), (1, 0)], [(1, 1)]]
    color_data, palette = make_lines(tiling, size, thickness)
    assert len(color_data) == expected_height
    assert len(color_data[0]) == expected_width
    assert len(palette) == 2, str(palette)


def test_make_black_lines_with_thickness_check_nodes():
    size, thickness = 10, 3
    expected_width = 4 * size + thickness
    expected_height = 4 * size + thickness
    tiling = [[(0, 0), (0, 1), (1, 0)], [(1, 1)]]
    color_data, palette = make_lines(tiling, size, thickness)
    for i in [size, size * 2, size * 3]:
        for j in [size, size * 2, size * 3]:
            assert color_data[i][j] == 1
    indices = [size - 1, size + thickness, size * 2 - 1, size * 2 + thickness, size * 3 - 1, size * 3 + thickness]
    for i in indices:
        for j in indices:
            assert color_data[i][j] == 0


def test_make_black_lines_with_thickness_check_strip():
    size, thickness = 10, 3
    expected_width = 4 * size + thickness
    expected_height = 4 * size + thickness
    tiling = [[(0, 0), (0, 1), (1, 0)], [(1, 1)]]
    color_data, palette = make_lines(tiling, size, thickness)
    margin = [0] * size
    line = [1] * thickness
    no_line = [0] * thickness
    square = [0] * (size - thickness)
    assert color_data[size + thickness] == margin + line + square + no_line + square + line + margin
