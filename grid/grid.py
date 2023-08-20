import random

import animals.elephant as elephant
import landscape.landscape_objs as landscape_objs
import color_palette

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
    
    def add_to_random_spot(self, obj):
        empty_spots = self.get_all_empty_xy()
        x, y = random.choice(empty_spots)
        print(f"location: {x}:{y} of {obj.name}")
        self.add(x, y, obj)

    def clean_objs(self):
        for x, y, obj in self.get_objs_with_xy():
            if not obj.alive:

                if obj.__class__ == landscape_objs.LandscapeObj:
                    self.add_to_random_spot(landscape_objs.LandscapeObj.create_new_random_landscape_obj())

                self.remove(x,y)

    # x, y - coordinates
    def get(self, x, y):
        if not (0 <= x < self.x and 0 <= y < self.y):
            raise ValueError("Invalid coordinates")
        return self.grid[y][x]

    def get_color(self, obj):
        res =  obj.get_status()
        if res == "baby":
            return color_palette.yellow_rgb
        elif res == "mature":
            return color_palette.light_pink_rgb
        elif res == "dying" or res == "dead" or res == "landscape":
            return color_palette.base_blue_rgb

        raise ValueError("Invalid status: %s" % res)
        
    def get_coordinates(self):
        self.tick()
        # clean
        self.clean_objs()
        return [
            (x, y, self.get_color(obj), self.get_description(obj), self.get_image(obj), self.get_id(obj), self.get_img_size(obj), self.needs_age_bar(obj), self.get_failures(obj))
            for (x,y,obj) in self.get_objs_with_xy()
        ]
    
    def get_failures(self, obj):
        if obj.__class__ == elephant.Elephant:
            return obj.get_obj_failures()
        else:
            return False
    
    def needs_age_bar(self, obj):
        if obj.__class__ == landscape_objs.LandscapeObj:
            return False
        else:
            return True

    
    def get_description(self, obj):
        return str(obj.get_obj_description())
    
    def get_empty_spots(self, objs):
        res = []
        for x,y,obj in objs:
            if obj is None:
                res.append((x,y))
        return res
    
    def get_id(self, obj):
        return str(obj.get_obj_id())
    
    def get_image(self, obj):
        return str(obj.get_obj_image())
    
    def get_img_size(self, obj):
        if obj.__class__ == elephant.Elephant:
            return "small"
        else:
            return "full"
    
    def get_neighbors(self, x, y):
        res = []
        y_checked = []
        x_checked = []

        for num in range(y-1, y + 2):
            if num >= 0 and num < self.y:
                y_checked.append(num)
            if num == self.y:
                y_checked.append(num - 1)
        
        for num in range(x-1, x + 2):
            if num >= 0 and num < self.x:
                x_checked.append(num)
            if num == self.x:
                x_checked.append(num - 1)
        
        y_min = min(y_checked)
        y_max = max(y_checked) + 1

        x_min = min(x_checked)
        x_max = max(x_checked) + 1

        # print(f"check coords:\n x:y: {x}:{y}\n y_checked: {y_checked} x_checked: {x_checked} y_min {y_min} y_max {y_max} x_min {x_min} x_max {x_max}")

        for count_row, row in enumerate(self.grid[y_min: y_max], y_min):
            for count_col, col in enumerate(row[x_min: x_max], x_min):
                if count_col == x and count_row == y:
                    continue
                res.append((count_col,count_row,col))
                # print(f"From get_neighbors: coord:{x}:{y}, res: {res}")
        return res
    
    def get_all_empty_xy(self):
        return [
            (count_col, count_row)
            for count_row, row in enumerate(self.grid)
            for count_col, col in enumerate(row)
            if(col is None)
        ]

    def get_objs_with_xy(self):
        # res = []
        # for count_row, row in enumerate(self.grid):
        #     for count_col, col in enumerate(row):
        #         if(col is not None):
        #             res.append((count_col, count_row, col))
        # return res
    
        return [
            (count_col, count_row, col)
            for count_row, row in enumerate(self.grid)
            for count_col, col in enumerate(row)
            if col is not None
        ]
    
    def get_occupied_spots(self, objs):
        # res = []
        # for x, y, obj in objs:
        #     if obj is not None:
        #         res.append((x, y, obj))
        # return res
    
        return [
            (x, y, obj) 
            for x, y, obj in objs 
            if obj is not None
        ]
    
    def get_pairs(self):
        res = []
        for x, y, obj in self.get_objs_with_xy():
            neighbors = self.get_neighbors(x, y)
            neighbors_occupied = self.get_occupied_spots(neighbors)
            for x2, y2, neighbor in neighbors_occupied:
                res.append(((x, y, obj),(x2, y2, neighbor)))
        return res

    def insert_near(self, coords, new_obj):
        neighbors = set()
        for x, y in coords:
            spots_all = self.get_neighbors(x,y)
            spots_free = self.get_empty_spots(spots_all)
            # print(f"all empty spots: {spots_free}")
            for spot in spots_free:
                neighbors.add(spot)

        # set comprehension
        # neighbors = {
        #     spot
        #     for x, y in coords
        #     for spot in self.get_empty_spots(self.get_neighbors(x,y))
        # }

        if neighbors:
            x, y = random.choice(list(neighbors))
            # print(f"chosen spot: {spot_to_insert}")
            # print(f"is it empty? {self.get(spot_to_insert[0],spot_to_insert[1])}")
            self.add(x, y, new_obj)
            # print(f"inserted object: {self.get(spot_to_insert[0],spot_to_insert[1])}")
        else:
            raise NoEmptySpotsException("No spots to insert")

    def move(self, x1, y1, x2, y2):
        # grab obj
        try:
            obj = self.get(x1,y1)
        except ValueError:
            return
        try:
            if obj.__class__ == landscape_objs.LandscapeObj:
                return
            else:
                self.add(x2,y2,obj)
                obj_in_new_spot = self.get(x2,y2)
                # if obj had usuccessful attempts to move before -> reset them
                obj_in_new_spot.failures = 0
        except OccupiedSpotsException:
            # add to counter for unsuccessful attempts
            obj.failures += 1
            obstacle = self.get(x2,y2)
            if obstacle.__class__ == landscape_objs.LandscapeObj:
                obstacle.receive_bump()
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
        for obj1, obj2 in self.get_pairs():
            # lanscape objs can't reproduce
            # if obj1.__class__ == "landscape_objs.LandscapeObj" or obj2.__class__ == "landscape_objs.LandscapeObj":
            #     return
            
            x1,y1,obj = obj1
            x2,y2,neighbor = obj2

            # print(f"print from reproduce_obj: OBJ1 ({x1}:{y1}) age {obj.age} sex {obj.sex}, OBJ2 ({x2}:{y2}) age {neighbor.age} sex {neighbor.sex}")

            if {(x1, y1), (x2, y2)}.intersection(served):
                continue
            try:
                res = obj.reproduce(neighbor)

                if res:
                    served.update({(x1, y1), (x2, y2)})

                for new_obj in res:
                    # print(f"This is new object:{new_obj}")
                    try:
                        self.insert_near([(x1, y1), (x2, y2)], new_obj)
                    except GridException:
                        pass
            except elephant.AnimalException:
                pass

            except landscape_objs.LandscapeObjsException:
                pass

    def tick(self):
        # move +1 to the right edge
        self.move_objs()
        # +1 to the age
        self.tick_objs()
        # reproduce objs
        self.reproduce_objs()
    
    def tick_objs(self):
        for _, _, obj in self.get_objs_with_xy():
            res = obj.tick()

            if res:
                print(f"print from grid: {res}")


class GridException(Exception):
    pass

class OccupiedSpotsException(GridException):
    pass

class NoEmptySpotsException(GridException):
    pass

class LandscapeMoveException(GridException):
    pass