from __future__ import annotations
from typing import Tuple, Callable, Dict, Any, NamedTuple
from .constants import GREEN, BLUE, YELLOW, RED, LAYOUT
from .worker import Worker

class Strategy(NamedTuple):
        name: str  
        fun: Callable 

class Player:

    __slots__ = 'teamColor', 'workers', 'strategy', 'memory'

    def __init__(self, strategy: Strategy, teamColor: Tuple[int, int, int]):
        self.strategy = strategy # namedtuple('Strategy', ['name', 'fun'])
        self.memory: Dict[Any, Any] = dict()
        self.teamColor = teamColor

        if teamColor == GREEN:
            x = 3; y = 36   # left upper corner
        elif teamColor == BLUE:
            x = 36; y = 3   # right lower corner
        elif teamColor == YELLOW:
            x = 36; y = 36
        elif teamColor == RED:
            x = 3; y = 3
        '''
        LAYOUT   [-1,1]  [0,1]  [1,1]
                 [-1,0]  [x,y]  [1,0]
                [-1,-1] [0,-1] [1,-1]      
        '''
        player_layout = [[x + i,y + j] for i,j in LAYOUT]
        self.workers = [Worker(i, j, teamColor) for i,j in player_layout]
 
    def play(self, mapa: Board): 
        self.strategy.fun(mapa, self.workers, self.memory) 

    def __str__(self) -> str:
        color = {
            BLUE:    'BLUE',
            YELLOW:  'YELLOW',
            RED:     'RED',
            GREEN:   'GREEN'
        }[self.teamColor]

        return f"player {color}, strategy: {self.strategy.name}"
