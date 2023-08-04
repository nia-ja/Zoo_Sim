class Grid:
    # x - number of columns
    # y - number of rows
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[None]*x for i in range(y)]

    # x, y - coordinates
    def get(self, x, y):
        return self.grid[y][x]

    def add(self, x, y, obj):
        if self.grid[y][x] is not None:
            raise OccupiedSpotsException("Spot is already occupied")
        self.grid[y][x] = obj
         

    def remove(self, x, y):
        self.grid[y][x] = None

    def get_neighbors(self, x, y):
        pass

    def get_coordinates(self):
        res = []
        for count_row, row in enumerate(self.grid):
            for count_col, col in enumerate(row):
                if(col is not None):
                    res.append((count_col, count_row))
        return res
    
class OccupiedSpotsException(Exception):
    pass