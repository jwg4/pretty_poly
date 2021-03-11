from .tiling import Tiling


def make_design(tiles, ragged=True):
    tiling = Tiling(tiles)
    return tiling.abstract(ragged)
