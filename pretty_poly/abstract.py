from .tiling import Tiling


def make_design(tiles):
    tiling = Tiling(tiles)
    return tiling.abstract()
