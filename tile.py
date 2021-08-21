from const import *

class Tile:
    def __init__(self, row, col):
        self.color = WHITE
        self.row = row
        self.col = col
        self.neighbors = []
        self.total_rows = 38
        self.total_cols = 43

    def draw(self, dsp):
        pygame.draw.rect(dsp, self.color, [self.col*TILE_SIZE+1, self.row*TILE_SIZE+1, TILE_SIZE-1, TILE_SIZE-1])

    def change_color(self, color):
        self.color = color
    
    def check_color(self):
        return self.color
    
    def get_neighbours(self, grid, diagonal):
        if self.row + 1 < self.total_rows and grid[self.row + 1][self.col].check_color() != BLACK: # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row - 1 >= 0 and grid[self.row - 1][self.col].check_color() != BLACK: # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col + 1 < self.total_cols and grid[self.row][self.col + 1].check_color() != BLACK: # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col - 1 >= 0 and grid[self.row][self.col - 1].check_color() != BLACK: # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

        

        if diagonal:
            # Left - down, left - up
            if self.col - 1 >= 0:
                if self.row + 1 < self.total_rows and grid[self.row + 1][self.col - 1].check_color() != BLACK and (grid[self.row + 1][self.col].check_color() != BLACK or grid[self.row][self.col - 1].check_color() != BLACK):
                    self.neighbors.append(grid[self.row + 1][self.col - 1])

                if self.row - 1 >= 0 and grid[self.row - 1][self.col - 1].check_color() != BLACK and (grid[self.row - 1][self.col].check_color() != BLACK or grid[self.row][self.col - 1].check_color() != BLACK):
                    self.neighbors.append(grid[self.row - 1][self.col - 1])

            # Right - up, # Right - down
            if self.col + 1 < self.total_cols:
                if self.row - 1 >= 0 and grid[self.row - 1][self.col + 1].check_color() != BLACK and (grid[self.row - 1][self.col].check_color() != BLACK or grid[self.row][self.col + 1].check_color() != BLACK):
                    self.neighbors.append(grid[self.row - 1][self.col + 1])

                if self.row + 1 < self.total_rows and grid[self.row + 1][self.col + 1].check_color() != BLACK and (grid[self.row + 1][self.col].check_color() != BLACK or grid[self.row][self.col + 1].check_color() != BLACK):
                    self.neighbors.append(grid[self.row + 1][self.col + 1])
            
