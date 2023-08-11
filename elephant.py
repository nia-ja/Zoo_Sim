from enum import Enum
import random

Sex = Enum("Sex", "male female")

class Animal:
    def __init__(self, age, sex=Sex.male):
        self.age = age
        self.sex = sex
    
    def get_status(self):
        if self.age <= 1:
            return "baby"
        elif 2 <= self.age <=9:
            return "mature"
        elif self.age == 10:
            return "dying"
        else:
            return "dead"
    
    @property
    def alive(self):
        return self.get_status() != "dead"

    def reproduce(self, partner):
        if self.__class__ != partner.__class__:
            raise IncompatibleBioTypeException("Wrong animal type")
        
        if self.sex == partner.sex:
            raise IncompatibleSexException("Wrong sex")
        
        if not self.alive or not partner.alive:
            raise DeadAnimalException("You animal or animals are dead")
        
        # randomizer for picking a sex of a new animal
        baby_sex = random.choice(list(Sex))
    
        # a randomizer for creating one or more animals at a time
        babies_num = random.randint(1,3)

        return set([self.__class__(0, sex=baby_sex) for _ in range(babies_num)])
    
    def tick(self):
        self.age+=1
    
class Elephant(Animal):
    pass

class IncompatibleBioTypeException(Exception):
    pass

class IncompatibleSexException(Exception):
    pass

class DeadAnimalException(Exception):
    pass