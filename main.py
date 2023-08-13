import random

# import elephant
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
            try:
                # add elephant to the grid
                my_grid.add(x, y, eleph)
                print(eleph.id)
            # try again
            except grid.OccupiedSpotsException:
                pass
            # exit loop
            else:
                break

    res = my_grid.grid

    for row in res:
        print(row)

    gui.grid_gui(my_grid.x, my_grid.y, my_grid.get_coordinates)

if __name__ == '__main__':
    main()