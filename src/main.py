import pygame
import sys
from Board import Board

def play() -> None:
    """
    Function that runs Main Menu.
    """
    board = Board(resolution[0],resolution[1]-60)
    
    
    while True:
        canvas.fill("#0065B7")
        topBar.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.click(mx,my)
                    
        text = "Turn: Red" if board.turn else "Turn: Yellow"           
        turnText = font.render(f"{text}", True, "#b68f40")
        turnRect = turnText.get_rect(center=(resolution[0]/2, 30))
        topBar.blit(turnText, turnRect)            
        
        result = board.isWin()
        
        pygame.display.update()
        board.draw(canvas)
        screen.blit(canvas, (0, 60))
        screen.blit(topBar, (0, 0))
        
        if result != None:
            winScreen(result)
            break
        
def winScreen(text) -> None:
    while True:
        topBar.fill((0,0,0))
        
        if text == True:
            text = "Red Wins"
        elif text == False:
            text = "Yellow Wins"
        
        menu_text = font.render(f"{text}", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(resolution[0]/2, 30))
        topBar.blit(menu_text, menu_rect)
        screen.blit(topBar, (0, 0))

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
    canvas = pygame.Surface((resolution[0], resolution[1]-60)) 
    topBar = pygame.Surface((resolution[0], 60)) 
    
    play()