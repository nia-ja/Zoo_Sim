import random
import math

import grid.grid as grid
import gui
import landscape.landscape as landscape
import animals.pack as pack

def main():
    screen_width, screen_height, block_size = gui.get_screen_size()
        
    # print(f"width: {screen_width}, height: {screen_height}, block_size: {block_size}")

    cols = math.floor(screen_width / block_size) - 1
    rows = math.floor(screen_height / block_size) - 2

    # temp
    # cols = 9
    # rows = 6

    # print(f"cols: {cols}, rows: {rows}")

    my_grid = grid.Grid(cols,rows)

    # return number of objs depending on grid size
    obj_number = (cols * rows) // 10

    # create a pack of random animals
    elephant_pack = pack.get_pack(obj_number - 7)


    # create a landscape
    landscape_objs = landscape.get_objs(obj_number - 2)

    all_objs = elephant_pack + landscape_objs

    # add each animal in the pack to the grid
    for item in all_objs:
        for _ in range(10):
            # get random coordinates
            x = random.randint(0, (cols - 1))
            y = random.randint(0, (rows - 1))
            try:
                # add elephant to the grid
                my_grid.add(x, y, item)
            # try again
            except grid.OccupiedSpotsException:
                pass
            # exit loop
            else:
                break

    res = my_grid.grid

    # for row in res:
        # print(row)

    gui.grid_gui(my_grid.x, my_grid.y, my_grid.get_coordinates, my_grid.get_all_empty_xy)

if __name__ == '__main__':
    main()