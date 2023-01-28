from __future__ import annotations
import pygame # type: ignore
from .constants import *
from .score import Scores
from typing import Tuple, List
from collections import deque


class Board:
    
    __slots__ = '__initBoard', '__visited', '__workers', '__board', \
                '__scoreGreen', '__scoreBlue', '__scoreRed', '__scoreYellow'

    ## --------------- CLASS SQUARE ------------------- ##
    class __Square:

        __slots__ = 'state', 'color'

        def __init__(self):
            self.state = True
            self.color = EMPTY
            
        def __bool__(self):
            return self.state
        
        def __repr__(self):
            return f"{self.color}"
    
    ## ---------------- CLASS BOARD ---------------------- ##
    def __init__(self):
        self._init()
        
    def _init(self):
        self.__visited = set()
        self.__board = [[self.__Square() for _ in range(COLS)] for _ in range(ROWS)]
        self.__workers = []
    
    # Get translated position color
    def __getitem__(self, coords: Tuple[int, ...]):
        match coords:
            case [x]:
                return EMPTY
            case [x, y]:
                squareColor = self.__board[ROWS-1-y][x].color
                return {  
                    SHADOWBLUE:   BLUE,
                    SHADOWGREEN:  GREEN,
                    SHADOWYELLOW: YELLOW,
                    SHADOWRED:    RED
                }.get(squareColor, squareColor)
    
    @property
    def workers(self):
        return tuple(self.__workers) 

    ## Get scores
    def _scores(self):
        return Scores(self.__scoreGreen, self.__scoreBlue, self.__scoreYellow, self.__scoreRed)
    
    ## DRAW
    def __draw_grid(self, win: 'pygame.display'):
        for i in range(ROWS+1):
            pygame.draw.line(win, EMPTY, (0, i * SQUARE_SIZE), 
                                         (HEIGHT, i * SQUARE_SIZE), GRID)
            for j in range(COLS+1):
                pygame.draw.line(win, EMPTY, (j * SQUARE_SIZE, 0),
                                            (j * SQUARE_SIZE, WIDTH), GRID)
    
    def _draw(self, win: 'pygame.display', replay: bool = False):
        self.__visited.clear()
        self.__scoreGreen  = 0
        self.__scoreBlue   = 0
        self.__scoreYellow = 0
        self.__scoreRed    = 0
           
        for row in range(ROWS):
            for col in range(COLS):
                square = self.__board[row][col]
                
                if square and not replay:
                    square.color = { 
                      BLUE:   SHADOWBLUE,
                      GREEN:  SHADOWGREEN,
                      YELLOW: SHADOWYELLOW,
                      RED:    SHADOWRED
                    }.get(square.color, square.color)
                    
                else:
                    square.state = True
                    
                pygame.draw.rect(win, square.color, 
                                (col * SQUARE_SIZE, 
                                 row * SQUARE_SIZE, 
                                 SQUARE_SIZE, SQUARE_SIZE))
                
                # ------------------------- SCORES ---------------------------- #
                
                if square.color is not EMPTY and (row, col) not in self.__visited:
                    self.__score_update(square, row, col)
                
        self.__draw_grid(win)


    ## UPDATE   
    def _update(self, workers: List[Worker]):
        # Pre: all workers are already validated
        for w in workers:
            row, col = w._coords()
            square = self.__board[row][col]
            square.color = w.color 
            square.state = False   
        self.__workers = workers
    
    # SCORE    
    def __score_update(self, square: __Square, row: int, col: int):
        if square.color in TEAMBLUE:
            color = TEAMBLUE
            score = self.__dfs((row, col), color)
            self.__scoreBlue  = max(self.__scoreBlue, score)
        
        elif square.color in TEAMGREEN:
            color = TEAMGREEN
            score = self.__dfs((row, col), color)
            self.__scoreGreen  = max(self.__scoreGreen, score)
        
        elif square.color in TEAMYELLOW:
            color = TEAMYELLOW
            score = self.__dfs((row, col), color)
            self.__scoreYellow  = max(self.__scoreYellow, score)
        
        elif square.color in TEAMRED:
            color = TEAMRED
            score = self.__dfs((row, col), color)
            self.__scoreRed  = max(self.__scoreRed, score)  
    
    
    # Get valid moves  
    def __valid_moves(self, coord) -> List[Tuple[int, int]]:
            row, col = coord
            lst = [(i + row,j + col) for i,j in VALIDMOVES]
            return [(row, col) for row, col in lst if row < 40 and row >= 0 and col < 40 and col >= 0]
    
    
    def __dfs(self, coords: Tuple[int, int], teamcolor: List[Tuple[int, int, int]]) -> int:
        s = deque([coords])
        self.__visited.add(coords)
        score = 1
        
        while s:
            node = s.pop()
            for neighbor in self.__valid_moves(node):
                row, col = neighbor
                if not neighbor in self.__visited and self.__board[row][col].color in teamcolor:
                    s.append(neighbor)
                    score += 1
                    self.__visited.add(neighbor)

        return score
