import logging

from pretty_poly.abstract import make_design


TILES = [
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(2, 2), (2, 1), (2, 0), (1, 2)]
]


def test_simple_tiling():
    logging.basicConfig(level=logging.DEBUG)
    faces, bars, lines, nodes = make_design(TILES)
    assert faces == [
        [0, 0, 1],
        [0, -1, 1],
        [0, 1, 1],
    ]
