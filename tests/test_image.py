from pretty_poly.image import make_colored_blocks


def test_make_colored_blocks():
    tiling = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(1, 0), (2, 0), (2, 1), (3, 0)]
    ]
    color_data, palette = make_colored_blocks(tiling)
    assert len(color_data) == 30
    assert len(color_data[0]) == 40
    assert len(palette) == 3, str(palette)
