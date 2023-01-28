from __future__ import annotations
from .constants import *
import pygame # type: ignore
import sys
from typing import NamedTuple, List
pygame.font.init()

class Scores(NamedTuple):
    green: int 
    blue: int 
    yellow: int 
    red: int

class Score():
    def __init__(self, x = 900, y = 500, width = 95, height = 200): 
        self.x   = x
        self.y   = y
        self.width = width
        self.height = height
        
    def _init(self, win: 'pygame.display', ticks: int):
        self.draw_bar(win, self.x, 8, GREENBAR)
        self.draw_bar(win, self.x + 100, 8, BLUEBAR)
        self.draw_bar(win, self.x + 200, 8, YELLOWBAR)
        self.draw_bar(win, self.x + 300, 8, REDBAR)
        self.draw_ticks(win, ticks)
        
    def draw(self, win: 'pygame.display', scores: Scores, ticks: int, players: List[Player]):
        self.draw_bar(win, self.x, scores.green, GREENBAR)
        self.draw_bar(win, self.x + 100, scores.blue, BLUEBAR)
        self.draw_bar(win, self.x + 200, scores.yellow, YELLOW)
        self.draw_bar(win, self.x + 300, scores.red, REDBAR)
        self.draw_ticks(win, ticks)
        self.draw_strategies(win, players)
        
    def draw_bar(self, win: 'pygame.display', x: int, score: int, color):
        # draw empty space
        emptyRect = pygame.Rect((x, self.y-200), (self.width, 200))
        pygame.draw.rect(win, EMPTY, emptyRect)    
        
        # define bar
        height = score / (ROWS*COLS) * self.height
        barRect = pygame.Rect((x, self.y - height), (self.width, height))  

        # display
        pygame.draw.rect(win, color, barRect)
        self.draw_score(win, x, score)
        
    def draw_score(self, win: 'pygame.display', x: int, score: int):
        # draw empty space
        emptyRect = pygame.Rect((x, self.y), (self.width, 30))
        pygame.draw.rect(win, EMPTY, emptyRect)
    
        # define font        
        font = pygame.font.SysFont('couriernew', 23)
        text = font.render(str(score), 1, (255,255,255))
        
        win.blit(text, (x + (self.width/2 - text.get_width()/2), 
                             self.y - 85 + (self.height/2 - text.get_height()/2)))
                              
        
    def draw_ticks(self, win: 'pygame.display', ticks: int):
        if ticks % 10 == 0:
            # define font        
            font = pygame.font.SysFont('arial', 30)
            text = font.render(str(ticks), 1, (255,255,255))
            
            emptyRect = pygame.Rect((880 + ( 95/2 - text.get_width()/2),  
                                     500 + (200/2 - text.get_height()/2)), 
                                    (110, 40))
            
            pygame.draw.rect(win, EMPTY, emptyRect)
            
            win.blit(text, (900 + ( 95/2 - text.get_width()/2), 
                            500 + (200/2 - text.get_height()/2)))   
        
    def draw_strategies(self, win: 'pygame.display', players: List[Player]):
        height = [100+SQUARE_SIZE*i for i in range(4)]
        
        font = pygame.font.SysFont('arial', 15)

        for row, player in zip(height, players):
            pygame.draw.rect(win, player.teamColor, 
                                    (self.x, 
                                     row, 
                                     SQUARE_SIZE-GRID, SQUARE_SIZE-GRID))

            text = font.render(player.strategy.name, 1, (255,255,255))
            emptyRect = pygame.Rect((self.x + SQUARE_SIZE, row), (text.get_width(), text.get_height()))
            pygame.draw.rect(win, EMPTY, emptyRect)
            win.blit(text, (self.x + SQUARE_SIZE, row)) 

                
        

