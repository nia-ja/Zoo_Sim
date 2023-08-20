from enum import Enum
import random

Sex = Enum("Sex", "male female")

# todo: check what's static method and how to write it
# todo: add test
def is_good_for_sex(age):
    if age <= 2:
        return False
    if age > 9:
        return False
    return True

def id_gen(x=0):
    while True:
        yield x
        x += 1

class Animal:
    # next_id = 0
    _id = id_gen()

    def __init__(self, age, sex=Sex.male):
        self.age = age
        self.sex = sex
        self.id = next(self._id)
        self.failures = 0 # to count failures to move, 3 - max
    
    # todo add test
    @property
    def alive(self):
        return self.get_status() != "dead"
    
    # todo add test
    def get_obj_description(self):
        return self.age
    
    def get_obj_failures(self):
        return self.failures
    
    # todo add test
    def get_obj_id(self):
        return self.id
    
    # todo add test
    def get_obj_image(self):
        if self.age >= 10:
            return "img/elephant/elephant.png"
        else:
            if self.sex == Sex.male:
                return "img/elephant/elephant_purple.png"
            else:
                return "img/elephant/elephant_pink.png"

    # todo add test
    def get_status(self):
        if self.age <= 2:
            return "baby"
        elif 3 <= self.age <=9:
            return "mature"
        elif self.age == 10:
            return "dying"
        else:
            return "dead" 

    def reproduce(self, partner):
        if self.__class__ != partner.__class__:
            raise IncompatibleBioTypeException("Wrong animal type")
        
        if self.sex == partner.sex:
            raise IncompatibleSexException("Wrong sex")
        
        if not self.alive or not partner.alive:
            raise DeadAnimalException("You animal or animals are dead")
        
        # todo add test
        if  not is_good_for_sex(self.age) or not is_good_for_sex(partner.age) :
            raise IncompatibleAgeException("Too old or too young for reproduction")
        
        # randomizer for picking a sex of a new animal
        baby_sex = random.choice(list(Sex))
    
        # a randomizer for creating one or more animals at a time
        babies_num = random.randint(0,2)
        # print(f"Parent 1: age {self.age}, sex {self.sex}, parent 2: age: {partner.age}, sex {partner.sex}")
        # print(f"Number of babies: {babies_num}")

        return set([self.__class__(0, sex=baby_sex) for _ in range(babies_num)])
    
    # todo add test
    def tick(self):
        # check if failed to move too much
        if self.failures > 3:
            self.age = 11

        self.age += 1

class Elephant(Animal):
    pass

class AnimalException(Exception):
    pass

class IncompatibleBioTypeException(AnimalException):
    pass

class IncompatibleSexException(AnimalException):
    pass

class DeadAnimalException(AnimalException):
    pass

class IncompatibleAgeException(AnimalException):
    pass