import unittest

import grid

class TestGrid(unittest.TestCase):
    def test_grid_creates_on_init(self):
        g = grid.Grid(3,2)
        self.assertEqual([[None, None, None], [None, None, None]], g.grid)

    def test_grid_returns_obj(self):
        g = grid.Grid(3,2)
        obj = g.get(1,2)
        self.assertEqual(None, obj)

    def test_grid_adds_obj(self):
        g = grid.Grid(3,2)
        obj = "New Object"
        g.add(1, 2, obj)
        res = g.get(1, 2)
        self.assertEqual(obj, res)

    def test_grid_removes_obj(self):
        g = grid.Grid(3,2)
        g.add(1, 2, "New Object")
        g.remove(1, 2)
        res = g.get(1, 2)
        self.assertEqual(None, res)


if __name__ == '__main__':
    unittest.main()