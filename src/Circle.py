from pygame import draw

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

        return (self.x,self.y)

    def getCenter(self) -> tuple:

        return (self.x+self.width/2, self.y+self.height/2)

    def draw(self,screen) -> None:
        if self.occupiedPiece == None:
            draw.circle(screen, center = self.getCenter() , radius = self.pieceRadius, color= "#1F1F1F")
        elif self.isHighlight:
            draw.circle(screen,center = self.getCenter(),radius = self.pieceRadius, color= "#2DC483")
        else:
            if self.occupiedPiece == True:
                draw.circle(screen,center = self.getCenter(),radius = self.pieceRadius, color= "#E71D36")
            else:
                draw.circle(screen,center = self.getCenter(),radius = self.pieceRadius, color= "#FFAA33")
                
        
