import logging


class Tiling(object):
    def __init__(self, tiles):
        logging.debug("Initializing tiling - tiles: %s" % (tiles,))
        self.tiles = tiles
        self.squares = [sq for tile in tiles for sq in tile]
        logging.debug("Initializing tiling - squares: %s" % (self.squares,))
        self.min_x = min(x for x, y in self.squares)
        self.min_y = min(y for x, y in self.squares)
        self.max_x = max(x for x, y in self.squares)
        self.max_y = max(y for x, y in self.squares)

    def format_row_sides(self, row):
        return " ".join("|" if r else " " for r in row)

    def format_row_upper(self, row):
        return "+" + "+".join("-" if r else " " for r in row) + "+"

    def format_tiling_lines(self, h, v):
        for i in range(0, self.max_y - self.min_y + 1):
            yield self.format_row_upper(h[i])
            yield self.format_row_sides(v[i])
        yield self.format_row_upper(h[self.max_y - self.min_y + 1])

    def make_base_h_row(self, i):
        lines_above = set(x for x, y in self.squares if y == i - 1)
        lines_below = set(x for x, y in self.squares if y == i)
        lines = lines_above.union(lines_below)

        return [(x in lines) for x in range(self.min_x, self.max_x + 1)]

    def make_base_v_row(self, i):
        lines_left = set(x for x, y in self.squares if y == i)
        lines_right = set(x + 1 for x, y in self.squares if y == i)
        lines = lines_left.union(lines_right)

        return [(x in lines) for x in range(self.min_x, max(lines) + 1)]

    def calculate_tiling(self):
        h = [self.make_base_h_row(i) for i in range(self.min_y, self.max_y + 2)]
        v = [self.make_base_v_row(i) for i in range(self.min_y, self.max_y + 1)]

        for tile in self.tiles:
            for sq_a in tile:
                for sq_b in tile:
                    a, b = sorted([sq_a, sq_b])
                    ax, ay = a[0] - self.min_x, a[1] - self.min_y
                    bx, by = b[0] - self.min_x, b[1] - self.min_y
                    if (ay == by) and (ax + 1 == bx):
                        v[ay][bx] = False
                    if (ax == bx) and (ay + 1 == by):
                        h[by][ax] = False

        return h, v

    def row_max(self, i):
        return max(sq[0] for sq in self.squares if sq[1] == i)

    def faces(self, ragged):
        if ragged:
            faces = [
                [-1 for i in range(self.min_x, self.row_max(j) + 1)]
                for j in range(self.min_y, self.max_y + 1)
            ]
        else:
            faces = [
                [-2 for i in range(self.min_x, self.max_x + 1)]
                for j in range(self.min_y, self.max_y + 1)
            ]

        for i, tile in enumerate(self.tiles):
            for sq in tile:
                faces[sq[1] - self.min_y][sq[0] - self.min_x] = i

        for x, y in self.open_blanks():
            faces[y - self.min_y][x - self.min_x] = -2

        return faces

    def open_blanks(self):
        s = set()
        sqs = set(self.squares)
        queue = (
            [(x, self.min_y) for x in range(self.min_x, self.row_max(self.min_y) + 1)]
            + [(self.min_x, y) for y in range(self.min_y + 1, self.max_y)]
            + [
                (x, y)
                for y in range(self.min_y + 1, self.max_y)
                for x in range(
                    min(self.row_max(y - 1), self.row_max(y + 1)), self.row_max(y) + 1
                )
            ]
            + [(x, self.max_y) for x in range(self.min_x, self.row_max(self.max_y) + 1)]
        )

        for sq in queue:
            if sq in sqs:
                continue
            s.add(sq)
            for x, y in self.neighbours(sq):
                if self.min_y <= y <= self.max_y:
                    if self.min_x <= x <= self.row_max(y):
                        if (x, y) not in s:
                            queue.append((x, y))

        return s

    @staticmethod
    def neighbours(sq):
        x, y = sq
        yield (x - 1, y)
        yield (x + 1, y)
        yield (x, y - 1)
        yield (x, y + 1)

    def nodes(self):
        nodes = [
            [0 for i in range(self.min_x - 1, self.max_x + 1)]
            for j in range(self.min_y - 1, self.max_y + 1)
        ]

        for i, row in enumerate(self.v):
            for j, bar in enumerate(row):
                if bar:
                    nodes[i][j] += 4
                    nodes[i + 1][j] += 1

        for i, row in enumerate(self.h):
            for j, bar in enumerate(row):
                if bar:
                    nodes[i][j] += 2
                    nodes[i][j + 1] += 8

        return nodes

    def abstract(self, ragged=True):
        self.h, self.v = self.calculate_tiling()
        return self.faces(ragged), self.v, self.h, self.nodes()
