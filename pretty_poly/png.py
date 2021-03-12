import png

from .image import make_colored_blocks, make_lines, make_blocks_and_lines


def _make_png_writer(data, palette):
    height = len(data)
    width = len(data[0])
    writer = png.Writer(width=width, height=height, palette=palette)
    return writer


def _write_png(filename, writer, data):
    with open(filename, "wb") as f:
        writer.write(f, data)


def write_colored_blocks_png(filename, tiling, scale=10):
    data, palette = make_colored_blocks(tiling, scale)
    writer = _make_png_writer(data, palette)
    _write_png(filename, writer, data)


def write_lines_png(filename, tiling, scale=10, width=1):
    data, palette = make_lines(tiling, scale, width)
    writer = _make_png_writer(data, palette)
    _write_png(filename, writer, data)
