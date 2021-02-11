from .abstract import make_design


def make_ascii(tiling):
    return "\n".join(gen_ascii(tiling))


def gen_ascii(tiling):
    faces, vlines, hlines, nodes = make_design(tiling)
    for i in range(0, len(vlines)):
        node_chars = ["+" if node else " " for node in nodes[i]]
        v_chars = ["-" if h else " " for h in hlines[i]]
        row = alternate(node_chars, v_chars)
        yield "".join(row)

        yield " ".join(["|" if v else " " for v in vlines[i]])

    i = len(vlines)     
    node_chars = ["+" if node else " " for node in nodes[i]]
    v_chars = ["-" if h else " " for h in hlines[i]]
    row = alternate(node_chars, v_chars)
    yield "".join(row)


def alternate(first, second):
    n = len(first) + len(second)
    for i in range(0, n):
        if i % 2 == 0:
            yield first[i // 2]
        else:
            yield second[i // 2]
