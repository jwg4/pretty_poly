from pretty_polly.abstract import make_design


def test_simple_tiling():
    tiles = [
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(2, 2), (2, 1), (2, 0), (1, 2)]
    ]
    cells, bars, lines, nodes = make_design(tiles)
    assert len(cells) == 3
    assert cells == [
        [0, 0, 1],
        [0, -1, 1],
        [0, 1, 1],
    ]
