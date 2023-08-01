class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[None]*x]*y

    def get(self, x, y):
        return self.grid[y-1][x-1]

    def add(self, x, y, obj):
        self.grid[y-1][x-1] = obj

    def remove(self, x, y):
        self.grid[y-1][x-1] = None

    def get_neighbors(self, x, y):
        pass