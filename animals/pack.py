import random

import animals.elephant as elephant

def get_pack(num):
    res = []

    for i in range(num):
        # random age
        age = random.randint(0,2)
        # random sex
        sex = random.choice(list(elephant.Sex))
        random_elephant = elephant.Elephant(age, sex)
        res.append(random_elephant)

    return res