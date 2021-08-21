from const import *

class Button:
    def __init__(self, x, y, width, height, color, text, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = pygame.font.SysFont('Arial', 25)
        self.text = self.font.render(text, True, BLACK)
        self.function = function
    

    def draw(self, dsp):
        pygame.draw.rect(dsp, self.color, [self.x, self.y, self.width, self.height])
        dsp.blit(self.text, (self.x+5, self.y+13))

    def pressed(self):
        return self.function()

    def pressed_diagonal(self):
        if not self.function:
            self.function = True
            self.color = GREEN
        else:
            self.function = False
            self.color = GREY



class Algorithm_Progress:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 25)
        self.x = 700
        self.search = self.font.render("Searching!", True, BLACK)
        self.done = self.font.render("Done!", True, BLACK)
        self.waiting = (self.font.render("A*", True, BLACK), self.font.render("algorithm", True, BLACK))
        self.not_found = (self.font.render("Path not", True, BLACK), self.font.render("Found", True, BLACK))
        self.selected_algorithm = False

    def not_waiting(self, dsp, progress, result):

        if result[0] is False:
            dsp.blit(self.not_found[0], (self.x, 50))
            dsp.blit(self.not_found[1], (self.x + 20, 80))
            return

        if progress:
            dsp.blit(self.search, (self.x, 50))
        else:
            dsp.blit(self.done, (self.x, 50))

    def no_alg_pressed(self, dsp):
        dsp.blit(self.waiting[0], (self.x + 30, 50))
        dsp.blit(self.waiting[1], (self.x, 80))


