from pretty_poly import make_ascii


def test_small_square_tiling():
    tiling = [[(0, 0), (1, 1), (1, 0), (2, 0)], [(0, 3), (1, 2), (0, 2), (0, 1)], [(3, 3), (2, 2), (2, 3), (1, 3)], [(3, 0), (2, 1), (3, 1), (3, 2)]]
    expected = '+-+-+-+-+\n|     | |\n+-+ +-+ +\n| | |   |\n+ +-+-+ +\n|   | | |\n+ +-+ +-+\n| |     |\n+-+-+-+-+'
    actual = make_ascii(tiling)
    assert actual == expected 
