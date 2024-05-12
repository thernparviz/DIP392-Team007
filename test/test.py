import os
import sys  
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.append(src_path)

import unittest
import pygame
from main import play, winScreen 
import main
from Board import Board
from Circle import Circle

class TestConnectFour(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.display.set_mode((840,740))  # Set up a display for pygame to avoid errors
        self.board = Board(600, 600)

    def test_board_creation(self):
        self.assertEqual(len(self.board.circles), 7)
        self.assertEqual(len(self.board.circles[0]), 6)
        self.assertEqual(len(self.board.boardCalc()), 42)

    def test_circle_creation(self):
        circle = Circle(0, 0, 100, 100, (0, 0))
        self.assertEqual(circle.getCoordinates(), (0, 0))
        self.assertEqual(circle.getCenter(), (50, 50))

    def test_turn_change(self):
        initial_turn = self.board.turn
        self.board.click(100, 100)
        self.assertNotEqual(initial_turn, self.board.turn)
        
    def test_placement(self):   
        # pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(0, 70)))
        self.board.click(0, 70)
        self.assertNotEqual(self.board.circles[0][-1].occupiedPiece, None)
        
    def test_outside_click(self):   
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(0, 0)))
        self.assertEqual(self.board.circles[0][-1].occupiedPiece, None)

    def test_isWin(self):
        # Test vertical win
        for i in range(4):
            self.board.circles[0][i].occupiedPiece = True
        self.assertEqual(self.board.isWin(), True)

        # Test horizontal win
        for i in range(4):
            self.board.circles[i][0].occupiedPiece = False
        self.assertEqual(self.board.isWin(), False)

        # Test diagonal right-left win
        for i in range(4):
            self.board.circles[i][i].occupiedPiece = True
        self.assertEqual(self.board.isWin(), True)

        # Test diagonal left-right win
        for i in range(4):
            self.board.circles[3-i][3-i].occupiedPiece = False
        self.assertEqual(self.board.isWin(), False)

    def test_board_tie(self):
        # Test if the game correctly identifies a tie
        for row in range(7):
            self.board.circles[row][0].occupiedPiece = True if ( row) % 2 == 0 else False
        self.assertEqual(self.board.isWin(), "Tie")



if __name__ == '__main__':
    unittest.main()
