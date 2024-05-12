# DIP392-Team007
Link of the report - https://docs.google.com/document/d/1p_BCfIAZAdzXjYuRDhLMDpyRU4NJ_DeoM-lY2-BSeDQ/edit?usp=sharing

## How to play
After starting the game, player one (yellow) starts, then its player two (red) turn. 

Each player, on his turn, can place a piece (circle) on a column, which piece is placed from bottom to top. To place a piece, the player must click anywhere on the desired column. This will place the piece and give the turn to the next player.  

To win, a player must line up 4 of his pieces in a horizontal, vertical or diagonal position. The player who achieves this is the winner and the other player is the loser.

A tie occurs when both players fail to achieve the winning condition and the board is completely filled with pieces.

## How to run from source
- Download the code from the top right corner of github. Code -> Download ZIP
- Install python 3.11.4 if you don't have it already.
- Install pygame module. You can do it by running the command below on a terminal.
```cmd
pip install pygame
```
- Run main.py
```cmd
python src/main.py
```
Note: Make sure file structure look like this

    ├── lib                      
    │   ├── Board.py
    │   ├── Cirlce.py
    | 
    └── src
        └── main.py
    
    
