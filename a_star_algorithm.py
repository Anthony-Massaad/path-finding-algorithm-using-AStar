from const import *
from queue import PriorityQueue


def reconstruct_path(path, current_tile, draw):
	while current_tile in path:
         current_tile = path[current_tile]
         current_tile.change_color(PURPLE)
         draw()

def heuristic(p1, p2):
    """
        Get current distance between 2 points
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def A_star_algorithm(draw, grid, start, end):
    count = 0
    start_row, start_col = start
    end_row, end_col = end
    #Our open set to  add nodes in
    open_list = PriorityQueue()
    open_list.put((0, count, start))
    # Keep track of the best possible path by checking what tile came from what
    path = {}
    # g score tracks the current shortest distance between 2 nodes
    g_score = {tiles: float("inf") for rows in grid for tiles in rows}
    g_score[grid[start_row][start_col]] = 0
    # Tracks the predicted distance between 2 tiles
    f_score = {tiles: float("inf") for rows in grid for tiles in rows}
    f_score[grid[start_row][start_col]] = heuristic(start, end)
    
    # In parallel with the open list, to check if neighbors of tile in the open list
    open_list_hash = {grid[start_row][start_col]}

    while not open_list.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        row, col = open_list.get()[2]
        current_tile = grid[row][col]
        open_list_hash.remove(current_tile)

        if current_tile == grid[end_row][end_col]:
            reconstruct_path(path, current_tile, draw)
            grid[end_row][end_col].change_color(BLUE)
            grid[start_row][start_col].change_color(RED)
            return True
        
        #checks all the neighbors of the current tile, and checks if the
        # G score is less than the current g score from the set, then up date the new path
        # and calculate the new predicted distance
        for neighbor in current_tile.neighbors:
            # + 1 because we need to assume all edges at least have 1
            temp_g_score = g_score[current_tile] + 1 

            #if the g score is less than the neighbor g score, change the path
            if temp_g_score < g_score[neighbor]:
                path[neighbor] = current_tile
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic((neighbor.row, neighbor.col), end)
                if neighbor not in open_list_hash:
                    count += 1
                    open_list.put((f_score[neighbor], count, [neighbor.row, neighbor.col]))
                    open_list_hash.add(neighbor)
                    neighbor.change_color(GREEN)
        draw()
        
        if current_tile != grid[start_row][start_col]:
            current_tile.change_color(ORANGE)

    return False
