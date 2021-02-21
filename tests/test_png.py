from pretty_poly import make_png


def test_basic_png_right_size():
    tiling = [
        [(0, 1), (0, 0)],
        [(1, 1), (1, 0)]
    ]
    image = make_png(tiling)
    assert image.size == 13, 13
