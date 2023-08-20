from enum import Enum
import math
import random

Name = Enum("Name", "tree stone water")
def id_gen(x=0):
    while True:
        yield x
        x += 1

class LandscapeObj:
    _id = id_gen()

    def __init__(self, strength, name=Name.stone, status=True):
        self.strength = strength
        self.name = name
        self.status = status
        self.id = next(self._id)
        self.failures = 0
    
    @property
    def alive(self):
        return self.get_status() != "dead"
    
    def create_new_random_landscape_obj():
        # random strength
        strength = random.randint(1,3)
        # random sex
        name = random.choice(list(Name))
        res = LandscapeObj(strength, name)
        print(f"print from create: {res}")
        return res
    
    def get_obj_description(self):
        return math.floor(self.strength)
    
    def get_obj_id(self):
        return self.id
    
    def get_obj_image(self):
        if self.name == Name.stone:
            return "img/landscape/stone.png"
        elif self.name == Name.tree:
            return "img/landscape/tree.png"
        elif self.name == Name.water:
            return "img/landscape/water.png"
    
    def get_status(self):
        if self.status == True:
            return "landscape"
        else:
            return "dead"
    
    def reproduce(self, pair):
        raise NotAbleToReproduceException("Landscape can't reproduce")
    
    def receive_bump(self):
        if self.name == Name.stone:
            self.strength -= 0.1
        elif self.name == Name.water:
            self.strength -= 0.2
        elif self.name == Name.tree:
            self.strength -= 0.3
        
        self.update_status()
    
    def update_status(self):
        if self.strength < 0:
            print(f"deleted landscape obj with id {self.id} and type {self.name}. Final srtength was: {self.strength}")
            self.status = "False"
    
    def tick(self):
        # todo make strength grow till 5 max
        if self.strength < 5:
            self.strength += 0.05
            

# Exceptions
class LandscapeObjsException(Exception):
        pass

class NotAbleToReproduceException(LandscapeObjsException):
        pass