import time

import grid
import elephant
import gui

def main():
    my_grid = grid.Grid(8,10)
    # @TO-DO: randomizer for creating first Elephans
    first_elephant = elephant.Elephant(0, elephant.Sex.female)
    my_grid.add(2, 3, first_elephant)
    res = my_grid.grid
    print(res)
    
    # @TO-DO: refactor to use coordinates not blocks
    #  @TO-DO: renaming
    #  @TO-DO: add comments

    gui.grid_gui(my_grid)

if __name__ == '__main__':
    main()