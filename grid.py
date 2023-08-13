import random

import elephant

class Grid:
    # x - number of columns
    # y - number of rows
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[None]*x for i in range(y)]

    def add(self, x, y, obj):        
        if self.get(x, y):
            raise OccupiedSpotsException("Spot is already occupied")
        self.grid[y][x] = obj

    def clean_objs(self):
        for x, y, obj in self.get_objs_with_xy():
            if not obj.alive:
                self.remove(x,y)

    # x, y - coordinates
    def get(self, x, y):
        if not (0 <= x < self.x and 0 <= y < self.y):
            raise ValueError("Invalid coordinates")
        return self.grid[y][x]

    def get_color(self, obj):
        res =  obj.get_status()
        if res == "baby":
            return (255, 190, 11)
        elif res == "mature":
            return (244, 172, 183)
        elif res == "dying" or res == "dead":
            return (131, 56, 236)

        raise ValueError("Invalid status: %s" % res)
    
    def get_coordinates(self):
        self.tick()
        # clean
        self.clean_objs()
        return [
            (x, y, self.get_color(obj), self.get_description(obj), self.get_image(obj), self.get_id(obj))
            for (x,y,obj) in self.get_objs_with_xy()
        ]
    
    def get_description(self, obj):
        return str(obj.get_obj_description())
    
    def get_id(self, obj):
        return str(obj.get_obj_id())
    
    def get_image(self, obj):
        return str(obj.get_obj_image())
    
    def get_neighbors(self, x, y):
        pass

    def get_objs_with_xy(self):
        res = []
        for count_row, row in enumerate(self.grid):
            for count_col, col in enumerate(row):
                if(col is not None):
                    res.append((count_col, count_row, col))
        return res
    
    # todo: add functionality
    def insert_near(self, objs, new_obj):
        pass

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

    def move_objs(self):
        # move separate object
        for x,y,_ in self.get_objs_with_xy():
            x_shift = random.choice([-1, 0, 1])
            y_shift = random.choice([-1, 0, 1])
            self.move(x, y, x+x_shift, y+y_shift)

    def remove(self, x, y):
        self.grid[y][x] = None

    def reproduce_objs(self):
        served = set()
        # todo: add get_pairs
        # for obj1, obj2 in self.get_pairs():
        #     if {obj1, obj2}.intersection(served):
        #         continue
        #     try:
        #         res = obj1.reproduce(obj2)

        #         if res:
        #             served.update({obj1, obj2})

        #         for new_obj in res:
        #             try:
        #                 self.insert_near([obj1, obj2], new_obj)
        #             except GridException:
        #                 pass
        #     except elephant.AnimalException:
        #         pass

    def tick(self):
        # move +1 to the right edge
        self.move_objs()
        # +1 to the age
        self.tick_objs()
        # reproduce objs
        self.reproduce_objs()
    
    def tick_objs(self):
        for _, _, obj in self.get_objs_with_xy():
            obj.tick()


class GridException(Exception):
    pass

class OccupiedSpotsException(GridException):
    pass