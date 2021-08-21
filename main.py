from const import *
from tile import Tile
from a_star_algorithm import A_star_algorithm
from side_assessories import Button, Algorithm_Progress

pygame.init()
GAME_WIDTH = 800
GAME_HEIGHT = 608
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT+1))
pygame.display.set_caption("Path Finding Algorithm")


def total_reset(grid, progress, start_pos, end_pos, result):
    for row in grid:
        for tile in row:
            tile.change_color(WHITE)
            tile.neighbors.clear()
    progress.selected_algorithm = False
    start_pos.clear()
    end_pos.clear()
    result[0] = None

def path_reset(grid, progress, result):
    for row in grid:
        for tile in row:
            if tile.check_color() == BLUE or tile.check_color() == RED:
                continue
            tile.change_color(WHITE)
            tile.neighbors.clear()
    progress.selected_algorithm = False
    result[0] = None

def point_reset(grid, progress, start_pos, end_pos, result):
    for row in grid:
        for tile in row:
            if tile.check_color() == BLACK:
                continue
            tile.change_color(WHITE)
            tile.neighbors.clear()
    progress.selected_algorithm = False
    start_pos.clear()
    end_pos.clear()
    result[0] = None

def search_again(grid, progress, result):
    for row in grid:
        for tile in row:
            if tile.check_color() == BLACK or tile.check_color() == BLUE or tile.check_color() == RED:
                continue
            tile.change_color(WHITE)
            tile.neighbors.clear()
    progress.selected_algorithm = False
    result[0] = None


def draw_grid(dsp, gridWidth):
    rows_cols = gridWidth // TILE_SIZE
    for i in range(rows_cols + 1):
        pygame.draw.line(dsp, BLACK, (0, i*TILE_SIZE), (gridWidth, i*TILE_SIZE))
        pygame.draw.line(dsp, BLACK, (i*TILE_SIZE, 0), (i*TILE_SIZE, GAME_HEIGHT))
    

def draw(dsp, gridWidth, grid, buttons, progress, al_started, run_btn, diagonal_btn, instruction_font, result):
    dsp.fill(WHITE)
    draw_grid(dsp, gridWidth)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw(dsp)

    for button in buttons:
        button.draw(dsp)
    run_btn.draw(dsp)
    diagonal_btn.draw(dsp)

    if not progress.selected_algorithm:
        progress.no_alg_pressed(dsp)
    else:
        progress.not_waiting(dsp, al_started, result)
    
    instruction1 = instruction_font.render("Right click to", True, BLACK)
    instruction2 = instruction_font.render("Delete Tile", True, BLACK)
    dsp.blit(instruction1, (697, 0))
    dsp.blit(instruction2, (710, 22))
    pygame.draw.line(dsp, BLACK, (688, 50), (GAME_WIDTH, 50))
    pygame.display.update()


def initialize_grid():
    grid = []
    for i in range(44):
        lst = []
        for j in range(43):
            lst.append(Tile(i, j))
        grid.append(lst)
    return grid


def main(dsp, gridWidth):
    run = True
    start_pos = []
    end_pos = []
    al_started = False
    grid = initialize_grid()
    progress = Algorithm_Progress()
    diagonal_btn = Button(689, 480, 112, 64, GREY, "+ Diagonal", False)
    diagonal = False
    result = [None]
    run_btn = Button(689, GAME_HEIGHT-64, 112, 64, GREEN, "RUN", lambda : A_star_algorithm(lambda: draw(dsp, gridWidth, grid, lst_of_buttons, progress, al_started, run_btn, diagonal_btn, instruction_font, result), grid, start_pos, end_pos))
    lst_of_buttons = [
            Button(689, 120, 112, 64, GREY, "Reset", lambda: total_reset(grid, progress, start_pos, end_pos, result)),
            Button(689, 210, 112, 64, GREY, "Path Reset", lambda: path_reset(grid, progress, result)),
            Button(689, 300, 112, 64, GREY, "Pts Reset", lambda: point_reset(grid, progress, start_pos, end_pos, result)),
            Button(689, 390, 112, 64, GREY, "Re-Search", lambda: search_again(grid, progress, result))
        ]
    instruction_font = pygame.font.SysFont('Arial', 20)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x >= 689 and len(start_pos) > 0 and len(end_pos) > 0 and not progress.selected_algorithm:
                    if run_btn.x <= x <= run_btn.x+run_btn.width and run_btn.y <= y <= run_btn.y+run_btn.height:
                        al_started = True
                        progress.selected_algorithm = True
                        for row in grid:
                            for tiles in row:
                                tiles.get_neighbours(grid, diagonal)
                        result[0] = run_btn.pressed()
                        al_started = False
                        break
                if x >= 689 and not al_started:
                    for reset_btn in lst_of_buttons:
                        if reset_btn.x <= x <= reset_btn.x+reset_btn.width and reset_btn.y <= y <= reset_btn.y+reset_btn.height:
                            reset_btn.pressed()
                    
                    if diagonal_btn.x <= x <= diagonal_btn.x+diagonal_btn.width and diagonal_btn.y <= y <= diagonal_btn.y+diagonal_btn.height:
                        diagonal_btn.pressed_diagonal()
                        diagonal = not diagonal

                    
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < 688 and not progress.selected_algorithm:
            x, y = pygame.mouse.get_pos()
            grid_row = y // TILE_SIZE
            grid_col = x // TILE_SIZE

            if grid[grid_row][grid_col].check_color() != BLUE and not start_pos:
                grid[grid_row][grid_col].change_color(RED)
                start_pos = [grid_row, grid_col]
            elif grid[grid_row][grid_col].check_color() != RED and not end_pos:
                grid[grid_row][grid_col].change_color(BLUE)
                end_pos = [grid_row, grid_col]
            elif grid[grid_row][grid_col].check_color() != BLUE and grid[grid_row][grid_col].check_color() != RED:
                grid[grid_row][grid_col].change_color(BLACK)
        
        elif pygame.mouse.get_pressed()[2] and pygame.mouse.get_pos()[0] < 688 and not progress.selected_algorithm:
            x, y = pygame.mouse.get_pos()
            grid_row = y // TILE_SIZE
            grid_col = x // TILE_SIZE
            if grid[grid_row][grid_col].check_color() == RED:
                start_pos = []
            elif grid[grid_row][grid_col].check_color() == BLUE:
                end_pos = []
            grid[grid_row][grid_col].change_color(WHITE)

        draw(dsp, gridWidth, grid, lst_of_buttons, progress, al_started, run_btn, diagonal_btn, instruction_font, result)

    pygame.quit()

if __name__ in "__main__":
    main(screen, GRID_WIDTH)