class Tiling(object):
    def __init__(self, tiles)
        self.tiles = tiles
        self.squares = [sq for tile in tiles for sq in tiles]
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

    def calculate_tiling(self, tiling):
        h = [self.make_base_h_row(i) for i in range(self.min_y, self.max_y + 2)]
        v = [self.make_base_v_row(i) for i in range(self.min_y, self.max_y + 1)]

        for tile in tiling:
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

    def abstract(self):
        h, v = self.calculate_tiling(tiling)
        faces = [
            [0 for i in range(self.min_x, self.max_x + 1)]
            for j in range(self.min_y, self.max_y + 1
        ]
        return faces, v, h, []
