import pygame
import sys
from Board import Board

def play() -> None:
    """
    Function that runs Main Menu.
    """
    board = Board(resolution[0],resolution[1]-60)
    
    
    while True:
        canvas.fill((0,0,255))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.click(mx,my)

        board.draw(canvas)
        screen.blit(canvas, (0, 60))
        
        pygame.display.update()
        
        result = board.isWin()
        if result != None:
            print(result)
            break
        
def winScreen(text) -> None:
    """
    Runs the Win Screen

    Parameters:
        text (str): stores who won.
    """
    
    
    while True:
        screen.fill((0))
        mouse_pos = pygame.mouse.get_pos()


        menu_text = font.render(f"{text} Wins", True, "#b68f40")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    resolution = [840,740]
    clock = pygame.time.Clock()
    clock.tick(30)
    
    fontSize = resolution[1]//18
    font = pygame.font.SysFont("arialblack", fontSize)
    screen = pygame.display.set_mode((resolution[0], resolution[1]))
    canvas = pygame.Surface((resolution[0], resolution[1])) 
    
    play()