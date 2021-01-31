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


def test_simple_tiling_check_nodes():
    logging.basicConfig(level=logging.DEBUG)
    faces, bars, lines, nodes = make_design(TILES)
    assert nodes == [
        [6, 10, 14, 12],
        [5, 6, 13, 5],
        [5, 7, 9, 5],
        [3, 11, 10, 9]
    ]


def test_simple_tiling_check_size():
    logging.basicConfig(level=logging.DEBUG)
    faces, bars, lines, nodes = make_design(TILES)
    x, y = len(faces[0]), len(faces)

    assert len(bars[0]) == x + 1 
    assert len(bars) == y

    assert len(lines[0]) == x
    assert len(lines) == y + 1

    assert len(nodes[0]) == x + 1 
    assert len(nodes) == y + 1
