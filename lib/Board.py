from Circle import Circle


class Board():

    
    def __init__(self, width: int, height: int, genSquares: bool = True):
       
        self.width = width
        self.height = height
        self.xSize = 6
        self.ySize = 7
        self.turn = False #False = player1, True = player2

        if genSquares:self.circles = self.genCirlces()
        else: self.circles = None

    def boardCalc(self) -> list:
        '''
        Calculates the square coordinates and sizes. Returns list containing coordinates, respect to width and height, and location.

        Returns:
                coordinate (list): Contains x,y coordinate and location for each square (x,y(row,column))
        '''
        
        coordinate = []
        
        self.increment_h = int(self.height/ self.xSize)
        self.increment_w = int(self.width/ self.ySize)
    
        # y = 0
        # for i in range(self.xSize):
        #     x = 0
        #     for j in range(self.ySize):
        #         coordinate.append((x,y,(i,j)))#location(row,column)
        #         x+=self.increment_w
        #     y+=self.increment_h
        # return coordinate
    
        x = 0
        for i in range(self.ySize):
            y = 0
            for j in range(self.xSize):
                coordinate.append((x,y,(j,i)))#location(row,column)
                y+=self.increment_h
            x+=self.increment_w
        return coordinate


    def genCirlces(self) -> list:
        '''
        Generates squares based on boardCalc() return. Returns lists within list containing Square objects.

        Returns:
                squares (list): Contains Square objects.
        '''
        circles = []
        coordinates = self.boardCalc()
        
        for j,coordinate in enumerate(coordinates):
            if j%self.xSize==0:
                circles.append([])

            circles[-1].append(Circle(coordinate[0],coordinate[1],self.increment_w,self.increment_h,coordinate[2]))
        return circles
    
    def getCircle(self,mx: int, my: int) -> Circle:
        '''
            Returns Square object based on mouse coordinates.

            Parameters:
                    mx (int): x coordinate
                    
                    my (int): y coordinate

            Returns:
                    square (Square): square object.
         '''
        y = my//self.increment_h 
        x = mx//self.increment_w
        return self.circles[y][x]


    def draw(self,screen) -> None:
        """
        Initiates draw sequence within Square objects.
        
        Parameters:
                screen (pygame.surface): window to draw
        """
        # if self.selectedPiece != None:
        #     for square in self.selectedPiece.posMoves(self):
        #         square.isHighlight = True

        for row in self.circles:
            for circle in row:
                circle.draw(screen)

    def click(self, mx: int, my: int) -> None:
        '''
            Handels mouse click on the game window.

            Parameters:
                    mx (int): x coordinate
                    
                    my (int): y coordinate
         '''
        colLocation = mx//self.increment_w #column number 0-6  increment = 900/7    128,57
        

        if self.circles[colLocation][0].occupiedPiece != None:
            #Stops the click function if the column is full
            return 

        for i in range(self.xSize):
            if self.circles[colLocation][i].occupiedPiece != None:
                self.circles[colLocation][i-1].occupiedPiece = self.turn
                self.turn = not self.turn                   
                return
            
        self.circles[colLocation][-1].occupiedPiece = self.turn
        self.turn = not self.turn
      
    def isWin(self):

        #vertical
        for col in range(self.ySize):
            for i in range(3):

                ith = self.circles[col][i].occupiedPiece

                if ith == None:
                    continue

                a= self.circles[col][i+1].occupiedPiece
                b= self.circles[col][i+2].occupiedPiece
                c= self.circles[col][i+3].occupiedPiece

                if ith == a == b == c:
                    self.highlight([self.circles[col][i],self.circles[col][i+1],self.circles[col][i+2],self.circles[col][i+3]])
                    return ith
        
        #horizontal
        for row in range(self.xSize):
            for i in range(4):

                ith = self.circles[i][row].occupiedPiece

                if ith == None:
                    continue

                a= self.circles[i+1][row].occupiedPiece
                b= self.circles[i+2][row].occupiedPiece
                c= self.circles[i+3][row].occupiedPiece

                if ith == a == b == c:
                    self.highlight([self.circles[i][row],self.circles[i+1][row],self.circles[i+2][row],self.circles[i+3][row]])
                    return ith

        #diagonal right-left
        for i in range(3):
            for j in range(4):

                ith = self.circles[j][i].occupiedPiece

                if ith == None:
                    continue

                a= self.circles[j+1][i+1].occupiedPiece
                b= self.circles[j+2][i+2].occupiedPiece
                c= self.circles[j+3][i+3].occupiedPiece

                if ith == a == b == c:
                    self.highlight([self.circles[j][i],self.circles[j+1][i+1],self.circles[j+2][i+2],self.circles[j+3][i+3]])
                    return ith
        
        #diagonal left-right
        for i in range(3):
            for j in range(4):

                ith = self.circles[j][self.xSize-1-i].occupiedPiece

                if ith == None:
                    continue

                a= self.circles[j+1][self.xSize-1-i-1].occupiedPiece
                b= self.circles[j+2][self.xSize-1-i-2].occupiedPiece
                c= self.circles[j+3][self.xSize-1-i-3].occupiedPiece

                if ith == a == b == c:
                    self.highlight([self.circles[j][self.xSize-1-i],self.circles[j+1][self.xSize-1-i-1],self.circles[j+2][self.xSize-1-i-2],self.circles[j+3][self.xSize-1-i-3]])
                    return ith

        #tie
        for row in range(self.ySize):
            if self.circles[row][0].occupiedPiece == None:
                return None 
            
        return "Tie"            

    def highlight(self, arr):
        for i in arr:
            i.isHighlight = True