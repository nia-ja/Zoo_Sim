import time

import grid
import elephant
import gui

def main():
    my_grid = grid.Grid(7,6)
    first_elephant = elephant.Elephant(0, elephant.Sex.female)
    my_grid.add(2, 3, first_elephant)
    res = my_grid.get(2,3)
    print(res.age)
    gui.grid_gui(my_grid.x, my_grid.y)
    # time.sleep(3)

if __name__ == '__main__':
    main()