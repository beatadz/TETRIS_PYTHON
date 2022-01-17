import pygame
import shapes

class NewShape(object):
    def __init__(self, grid):
        self.shape = []
        self.full_shape = []
        self.row = ""
        self.grid = grid
        self.new_shapes_colors = [[grid.main_color for x in range(4)] for y in range(4)]

    def save_shape(self, grid, nr):
        empty = True
        for i in range(0, 4):
            self.row = ""
            for j in range(0, 4):
                if grid.select[i][j] != grid.main_color:
                    self.new_shapes_colors[i][j] = grid.select[i][j]
                    self.row = self.row + "1"
                    empty = False
                else:
                    self.row = self.row + "0"
            self.shape.append(self.row)
        if empty is True:
            self.shape.clear()
            self.row = ""
        else:
            shapes.new_colors.append(self.new_shapes_colors)
            for i in range(0, 4): # na razie bez obracania
                self.full_shape.append(self.shape)
            print(self.full_shape)
            shapes.shapes.append(self.full_shape)

        return empty