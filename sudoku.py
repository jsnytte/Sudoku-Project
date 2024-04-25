import pygame
from sudoku_generator import SudokuGenerator, Board, Cell, generate_sudoku

def main():
    # init
    pygame.init()
    size = screen_width, screen_height = 650, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sudoku")

    # style
    title_font = pygame.font.SysFont("Courier New", 100)
    menu_font = pygame.font.SysFont("Courier New", 30)

    # surfaces
    title_surface = title_font.render("Sudoku!", 1, [64, 64, 64])
    easy_surface = menu_font.render(" Easy ", 1, [64, 64, 64], [255, 255, 255])
    medium_surface = menu_font.render(" Medium ", 1, [64, 64, 64], [255, 255, 255])
    hard_surface = menu_font.render(" Hard ", 1, [64, 64, 64], [255, 255, 255])    

    # rectangles
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    easy_rect = easy_surface.get_rect(center=(screen_width // 4, screen_height // 2))
    medium_rect = medium_surface.get_rect(center=(2 * screen_width // 4, screen_height // 2))
    hard_rect = hard_surface.get_rect(center=(3* screen_width // 4, screen_height // 2))
    
    # init new game
    board = Board(450, 450, screen, 30)
    game_state = "menu"
    program_run = True
    
    # main
    while program_run:
        if game_state == "menu":
            # window background
            screen.fill([200, 200, 200])
            screen.blit(title_surface, title_rect)
            screen.blit(easy_surface, easy_rect)
            screen.blit(medium_surface, medium_rect)
            screen.blit(hard_surface, hard_rect)

            if easy_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    difficulty = 30
                    game_state = "game"
            if medium_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    difficulty = 40
                    game_state = "game"
            if hard_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    difficulty = 50
                    game_state = "game"
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        
        # game screen
        if game_state == "game":
            board = Board(450, 450, screen, difficulty) 
            screen.fill([200,200,200])
            # board.draw
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    
        pygame.display.update()
        
if __name__ == '__main__':
    main()
