import pygame # type: ignore
from .constants import *
from .board import Board
from .score import Score
from .players import Players
from copy import deepcopy

class Game:
    
    __slots__ = 'WIN', 'maxticks', 'board', 'score', 'players', 'ticks', \
                'allFrames', 'frame'

    def __init__(self, maxticks, WIN, strategies):
        self.WIN = WIN
        self.maxticks = maxticks
        self.board = Board()
        self.score = Score()
        self.players = Players(strategies)
        self.new_game()
        
    def new_game(self): 
        # Reset every class
        self.score._init(self.WIN, 0)
        self.board._init()
        self.players._init()

        # Define variables
        self.ticks = -1        
        self.allFrames = []
        
        # First move to update board 
        # with starting poisitions
        self.play()

    def play(self):
        # Update workers positions on board
        self.board._update(self.players.getPlayersWorkers())
        
        # Display on screen
        self.board._draw(self.WIN)
        self.score.draw(self.WIN, self.board._scores(), self.ticks, self.players.players)  
        
        copyBoard = deepcopy(self.board)
        
        if self.ticks < self.maxticks:
            self.ticks += 1
            self.players.play(copyBoard)
            self.allFrames.append(copyBoard)
        self.frame = self.ticks

    def backward(self): # Replay backwards
        self.frame -= 1 if self.frame > 0 else 0
        try:
            self.allFrames[self.frame]._draw(self.WIN, replay = True)
            self.score.draw(self.WIN, self.allFrames[self.frame]._scores(), self.frame, self.players.players)
        except IndexError:
            pass
        
    def forward(self): # Replay forwards
        self.frame += 1 if self.frame < len(self.allFrames)  else 0
        try: 
            self.allFrames[self.frame]._draw(self.WIN, replay = True)
            self.score.draw(self.WIN, self.allFrames[self.frame]._scores(), self.frame, self.players.players)
        except IndexError:
            pass
        