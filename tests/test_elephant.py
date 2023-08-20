import unittest
from unittest.mock import patch

import animals.elephant as elephant

class TestElephant(unittest.TestCase):
    def test_alive_for_baby(self):
        e = elephant.Elephant(1)
        self.assertTrue(e.alive)

    def test_alive_for_mature(self):
        e = elephant.Elephant(5)
        self.assertTrue(e.alive)
    
    def test_alive_for_dying(self):
        e = elephant.Elephant(10)
        self.assertTrue(e.alive)
    
    def test_alive_for_dead(self):
        e = elephant.Elephant(11)
        self.assertFalse(e.alive)

    def test_age_on_init(self):
        e = elephant.Elephant(1)
        self.assertEqual(1, e.age)

    def test_sex_on_init(self):
        e = elephant.Elephant(1, elephant.Sex.female)
        self.assertEqual(elephant.Sex.female, e.sex)
    
    def test_reproduce_with_wrong_animal(self):
        e = elephant.Elephant(3)
        class Dog(elephant.Animal):
            pass
        d = Dog(4)
        self.assertRaises(elephant.IncompatibleBioTypeException, e.reproduce, d)
    
    def test_reproduce_with_wrong_sex(self):
        e1 = elephant.Elephant(3, elephant.Sex.female)
        e2 = elephant.Elephant(3, elephant.Sex.female)
        self.assertRaises(elephant.IncompatibleSexException, e1.reproduce, e2)
    
    def test_reproduce_with_dead_animal(self):
        e1 = elephant.Elephant(3, elephant.Sex.male)
        e2 = elephant.Elephant(11, elephant.Sex.female)
        self.assertRaises(elephant.DeadAnimalException, e1.reproduce, e2)
    
    def test_reproduce_when_dead(self):
        e1 = elephant.Elephant(11, elephant.Sex.male)
        e2 = elephant.Elephant(3, elephant.Sex.female)
        self.assertRaises(elephant.DeadAnimalException, e1.reproduce, e2)
    
    def test_reproduce_produces_a_child(self):
        e1 = elephant.Elephant(3, elephant.Sex.male)
        e2 = elephant.Elephant(3, elephant.Sex.female)

        babies = e1.reproduce(e2)

        self.assertTrue(babies)

        for baby in babies:
            self.assertEqual(0, baby.age)
            self.assertTrue(isinstance(baby, elephant.Elephant))
    
    def test_reproduce_returns_chosen_sex(self):
        e1 = elephant.Elephant(3, elephant.Sex.male)
        e2 = elephant.Elephant(3, elephant.Sex.female)

        with patch("random.randint", return_value=1), patch("random.choice", return_value=elephant.Sex.male):
            babies = e1.reproduce(e2)

        self.assertTrue(babies)

        for baby in babies:
            self.assertEqual(elephant.Sex.male, baby.sex)

    # no more then 2 babies
    def test_reproduce_returns_2_babies_or_less(self):
        e1 = elephant.Elephant(3, elephant.Sex.male)
        e2 = elephant.Elephant(3, elephant.Sex.female)

        babies = e1.reproduce(e2)

        self.assertLessEqual(len(babies), 2)


    # right amount of babies is born
    def test_reproduce_returns_right_amount_of_babies(self):
        e1 = elephant.Elephant(3, elephant.Sex.male)
        e2 = elephant.Elephant(3, elephant.Sex.female)

        with patch("random.randint", return_value=2):
            babies = e1.reproduce(e2)
        
        self.assertEqual(2, len(babies))



if __name__ == '__main__':
    unittest.main()