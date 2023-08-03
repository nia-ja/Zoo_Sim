class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[None]*x for i in range(y)]

    def get(self, x, y):
        return self.grid[y-1][x-1]

    def add(self, x, y, obj):
        self.grid[y-1][x-1] = obj

    def remove(self, x, y):
        self.grid[y-1][x-1] = None

    def get_neighbors(self, x, y):
        pass

    def get_coordinates(self):
        res = []
        for count_row, row in enumerate(self.grid):
            for count_col, col in enumerate(row):
                if(col is not None):
                    res.append((count_col + 1, count_row + 1))
        return res