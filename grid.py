import random

class Grid:
    # x - number of columns
    # y - number of rows
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[None]*x for i in range(y)]

    # x, y - coordinates
    def get(self, x, y):
        if not (0 <= x < self.x and 0 <= y < self.y):
            raise ValueError("Invalid coordinates")
        return self.grid[y][x]

    def add(self, x, y, obj):        
        if self.get(x, y):
            raise OccupiedSpotsException("Spot is already occupied")
        self.grid[y][x] = obj
         

    def remove(self, x, y):
        self.grid[y][x] = None

    def get_neighbors(self, x, y):
        pass

    def get_coordinates(self):
        self.tick()
        return [
            (x, y)
            for (x,y,obj) in self.get_objs_with_xy()
        ]
    
    def tick(self):
        # move +1 to the right edge
        self.move_objs()
        # +1 to the age
        self.update_properties()
    
    def move_objs(self):
        # move separate object
        for x,y,obj in self.get_objs_with_xy():
            x_shift = random.choice([-1, 0, 1])
            y_shift = random.choice([-1, 0, 1])
            self.move(x, y, x+x_shift, y+y_shift)
    
    def get_objs_with_xy(self):
        res = []
        for count_row, row in enumerate(self.grid):
            for count_col, col in enumerate(row):
                if(col is not None):
                    res.append((count_col, count_row, col))
        return res

    def move(self, x1, y1, x2, y2):
        # grab obj
        try:
            obj = self.get(x1,y1)
        except ValueError:
            return
        
        try:
            self.add(x2,y2,obj)
        except OccupiedSpotsException:
            return
        except ValueError:
            return
        
        self.remove(x1,y1)
    
    def update_properties(self):
        pass
    
class OccupiedSpotsException(Exception):
    pass