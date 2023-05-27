# CGOL

This program implements Conway's Game of Life using the Pygame library. The Game of Life is a cellular automaton devised by the mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game takes place on a grid of cells, where each cell can be in one of two states: alive or dead.
Installation

To run the program, you need to have Python and Pygame installed on your system. Pygame is a set of Python modules designed for writing video games.

   Install Python: You can download and install Python from the official website: https://www.python.org/downloads/

   Install Pygame: Open a terminal or command prompt and run the following command to install Pygame:

    pip install pygame

**How to Run**

To start the Game of Life simulation, follow these steps:

   Download the source code file (game_of_life.py) and any necessary assets (images) to your local machine.

   Open a terminal or command prompt and navigate to the directory where the source code file is located.

   Run the following command to start the program:

    python game_of_life.py

   The program window will open, displaying the initial state of the Game of Life grid.

**Game Controls**

The Game of Life program provides the following controls:

   Left Mouse Button: Click and drag to draw live cells on the grid.
   Right Mouse Button: Click and drag to erase cells from the grid.
   Space: Pause or resume the simulation.
   C: Clear the grid (set all cells to a dead state).

**Rules of the Game**

The Game of Life follows the following rules:

   Any live cell with fewer than two live neighbors dies, as if by underpopulation.
   Any live cell with two or three live neighbors survives to the next generation.
   Any live cell with more than three live neighbors dies, as if by overpopulation.
   Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

**Program Structure**

The source code file (game_of_life.py) consists of the following components:

   Imports: The necessary libraries are imported, including pygame and numpy.

   Initialization: The Pygame library is initialized, and the program window is set up. The required assets are loaded.

   GameOfLife Class: This class represents the Game of Life simulation. It contains methods for handling user input, updating the grid based on the game rules, and drawing the grid on the screen.
       __init__: Initializes the GameOfLife object and sets up the initial state.
       mouse_pos: Returns the grid position corresponding to the current mouse position.
       snap_cursor_to_grid: Calculates the position of the cursor on the grid.
       count_neighbors: Counts the number of live neighbors for each cell in the grid.
       update: Updates the grid based on the Game of Life rules.
       draw: Sets cells on the grid based on user input.
       play: Starts the main game loop.

   Main Execution: The GameOfLife class is instantiated, and the play method is called to start the simulation.

**Credits**

The program uses the Pygame library for graphical and input handling functionalities.
