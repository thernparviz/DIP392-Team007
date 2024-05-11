from pygame import Rect,draw

class Circle():
    
    def __init__(self,x: int, y: int, width: int, height: int, location: tuple):
        
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.location = location #location(row,column)
        
        self.occupiedPiece = None # False = 'yellow' True = 'red' 
        
        self.isHighlight = False
        
        # self.color = (209, 139, 71) if (location[0] + location[1]) % 2 == 0 else (255, 206, 158)				 
        self.pieceRadius = int((self.height/2)-(0.1*self.width))
        # self.pieceRadius = 10
        # self.rect = Rect(self.x,self.y,width,height)
    
    def getCoordinates(self) -> tuple:
        """
        Returns:
            coordinates (tuple) : coordinates(x,y)
        """
        return (self.x,self.y)

    def getCenter(self) -> tuple:
        """
        Returns: 
            center coordinates (tuple): center of the Square (x,y).
        """
        return (self.x+self.width/2, self.y+self.height/2)

    def draw(self,screen) -> None:
        """
        Handels the drawing of the Squares and Pieces on the game window.
        
        Parameters:
                screen (pygame.surface): window to draw
        """
        draw.circle(screen, center = self.getCenter() , radius = self.pieceRadius, color= (25,25,25))
        
        if self.occupiedPiece != None:
            if self.occupiedPiece == True:
                draw.circle(screen,center = self.getCenter(),radius = self.pieceRadius, color= "Red")
            else:
                draw.circle(screen,center = self.getCenter(),radius = self.pieceRadius, color= "Yellow")
