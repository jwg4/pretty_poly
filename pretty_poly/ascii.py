from .abstract import make_design


def make_ascii(tiling):
    return "\n".join(gen_ascii(tiling))


def gen_ascii(tiling):
    faces, vlines, hlines, nodes = make_design(tiling)
    for i in range(0, len(vlines)):
        node_chars = ["+" if node else " " for node in nodes[i]]
        h_chars = ["-" if h else " " for h in hlines[i]]
        row = alternate(node_chars, h_chars)
        yield "".join(row).rstrip()

        face_chars = ["X" if face == -1 else " " for face in faces[i]]
        v_chars = ["|" if v else " " for v in vlines[i]]
        row = alternate(v_chars, face_chars)
        yield "".join(row).rstrip()

    i = len(vlines)
    node_chars = ["+" if node else " " for node in nodes[i]]
    h_chars = ["-" if h else " " for h in hlines[i]]
    row = alternate(node_chars, h_chars)
    yield "".join(row).rstrip()


def alternate(first, second):
    assert len(second) in [len(first) - 1, len(first)]
    n = len(first) + len(second)
    for i in range(0, n):
        if i % 2 == 0:
            yield first[i // 2]
        else:
            yield second[i // 2]
