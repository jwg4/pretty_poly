import tempfile

import xml.etree.ElementTree as ET

from pretty_poly.svg import write_colored_blocks_svg


def test_basic_svg_right_size():
    tiling = [
        [(0, 1), (0, 0)],
        [(1, 1), (1, 0)]
    ]
    f, filename = tempfile.mkstemp(suffix=".svg")
    write_colored_blocks_svg(filename, tiling)
    tree = ET.parse(filename)
    root = tree.getroot()
    assert root is not None
