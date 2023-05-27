import pygame as pg
import numpy as np
from os import path

pg.init()
WIDTH, HEIGHT = 500, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game of Life")

# Load the image
image = pg.image.load(path.join('assets', 'cursor.png'))

hotspot = (10, 9)
pg.mouse.set_cursor(hotspot, image)


class GameOfLife:
    def __init__(self):
        self.cell_size = 5
        self.bg = (0, 0, 0)
        self.grid_width = WIDTH // self.cell_size
        self.grid_height = HEIGHT // self.cell_size
        self.grid = np.zeros((self.grid_width, self.grid_height))

        self.colors = {}
        self.play_area = pg.Rect(465, 465, 30, 30)
        self.kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        self.input_shape = np.array([[0, 1, 1],
                                     [1, 1, 0],
                                     [0, 1, 1]])

        self.btn_play = pg.image.load(path.join('assets', 'play2.png'))
        self.btn_pause = pg.image.load(path.join('assets', 'pause2.png'))

    def mouse_pos(self):
        pos = pg.mouse.get_pos()
        # Calculate corresponding grid position
        x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
        return x, y

    def snap_cursor_to_grid(self):
        # Calculate the position of the cursor on the grid
        x, y = self.mouse_pos()
        cursor_x = x * self.cell_size
        cursor_y = y * self.cell_size
        return cursor_x, cursor_y

    def count_neighbors(self):
        n = np.zeros_like(self.grid)

        # Loop over all cells in the kernel
        # Compute the sum of their values in the grid
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:  # Current cell
                    continue
                n += np.roll(self.grid, shift=(i - 1, j - 1), axis=(0, 1)) * self.kernel[i, j]
        return n

    # Update the grid based on the Game of Life rules
    def update(self, neighbors):
        # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        # Any live cell with more than three live neighbors dies, as if by overpopulation.
        mask = (self.grid == 1) & ((neighbors < 2) | (neighbors > 3))
        self.grid[mask] = 0
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        mask = (self.grid == 0) & (neighbors == 3)
        self.grid[mask] = 1

    def draw(self, state):
        x, y = self.mouse_pos()

        # Set the cells at the mouse position according to input shape
        shape_width, shape_height = self.input_shape.shape
        for i in range(shape_width):
            for j in range(shape_height):
                if self.input_shape[i, j] == 1:
                    # Check if input shape falls within grid boundary
                    if 0 <= x + i < self.grid.shape[0] \
                            and 0 <= y + j < self.grid.shape[1]:
                        # Set the value of the corresponding position in the grid to 1
                        self.grid[x + i, y + j] = state

    # Start the game loop
    def play(self):
        clock = pg.time.Clock()
        l_mouse_down = False
        r_mouse_down = False
        paused = False

        while True:
            # Loop through each cell in the grid
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):

                    if self.grid[i, j] == 1:  # is alive
                        if (i, j) not in self.colors:  # doesn't have a color

                            # Generate random color and add it to dict
                            self.colors[(i, j)] = (250, 250, 250)
                            # np.random.randint(50, 256),  # R
                            # np.random.randint(50, 256),  # G
                            # np.random.randint(50, 256))  # B

                        cs = self.cell_size
                        # Get color of the cell from the dict and draw a rectangle
                        color = self.colors[(i, j)]
                        pg.draw.rect(WIN, color, (i * cs, j * cs, cs, cs))

                    else:  # is dead
                        cs = self.cell_size
                        # Draw a rectangle the same color as the win bg to represent the dead cell
                        pg.draw.rect(WIN, self.bg, (i * cs, j * cs, cs, cs))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        l_mouse_down = True

                        if self.play_area.collidepoint(pg.mouse.get_pos()):
                            paused = not paused
                        else:
                            self.draw(1)

                    elif event.button == 3:
                        r_mouse_down = True
                        self.draw(0)

                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        l_mouse_down = False

                    elif event.button == 3:
                        r_mouse_down = False

                elif event.type == pg.MOUSEMOTION:
                    if l_mouse_down:
                        self.draw(1)
                    elif r_mouse_down:
                        self.draw(0)

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        paused = not paused

                    elif event.key == pg.K_c:
                        self.grid = np.zeros((self.grid_width, self.grid_height))

            self.snap_cursor_to_grid()

            if not paused:
                # Get number of live neighbors and update grid
                neighbor_count = self.count_neighbors()
                self.update(neighbor_count)
                WIN.blit(self.btn_play, self.play_area)

            else:
                WIN.blit(self.btn_pause, self.play_area)

            # Update the screen
            pg.display.update()
            clock.tick(15)


if __name__ == '__main__':
    gol = GameOfLife()
    gol.play()
