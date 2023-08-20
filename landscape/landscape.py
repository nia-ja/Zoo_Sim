import random

import landscape.landscape_objs as landscape_objs

def get_objs(num):
    res = []
    
    for i in range(num):
        # random strength
        strength = random.randint(1,3)
        # random sex
        name = random.choice(list(landscape_objs.Name))
        random_landscape_obj = landscape_objs.LandscapeObj(strength, name)
        res.append(random_landscape_obj)

    return res