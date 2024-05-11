import pygame
import sys
from Board import Board

def play() -> None:
    """
    Function that runs Main Menu.
    """
    board = Board(resolution[0],resolution[1])
    
    while True:
        screen.fill((0,0,255))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.click(mx,my)

        board.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    resolution = [900,720]
    
    clock = pygame.time.Clock()
    clock.tick(30)
    screen = pygame.display.set_mode((resolution[0], resolution[1]))
    play()