import random
import time

import elephant
import grid
import gui
import pack

def main():
    cols = 8
    rows = 10
    my_grid = grid.Grid(cols,rows)

    # return number of objs depending on grid size
    obj_number = (cols * rows) // 10

    # create a pack of random animals
    elephant_pack = pack.get_pack(obj_number)

    # add each animal in the pack to the grid
    for eleph in elephant_pack:
        for _ in range(10):
            # get random coordinates
            x = random.randint(0, (cols - 1))
            y = random.randint(0, (rows - 1))
            print([x,y])
            try:
                # add elephant to the grid
                my_grid.add(x, y, eleph)
            except grid.OccupiedSpotsException:
                pass
            else:
                break

    res = my_grid.grid

    for row in res:
        print(row)

    # @TO-DO: refactor to use coordinates not blocks
    #  @TO-DO: renaming
    #  @TO-DO: add comments

    gui.grid_gui(my_grid)

if __name__ == '__main__':
    main()