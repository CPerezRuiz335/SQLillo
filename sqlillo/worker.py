from .constants import VALIDMOVES, COLS, ROWS
from typing import List, Tuple

class Worker:
    
    __slots__ = '__x', '__y', '__prevX', '__prevY', '__color', '__h'

    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__prevX = x
        self.__prevY = y
        self.__color = color
        self.__h  = (self.__x, self.__y)
                
    # Getters
    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y
    
    @property
    def color(self) -> Tuple[int, int, int]:
        return self.__color

    def _coords(self) -> Tuple[int, int]:
        return (ROWS - self.__y - 1, self.__x)
        
    # Setters
    def _invalidate(self):
        self.__x = self.__prevX
        self.__y = self.__prevY
    
    def _validate(self):
        self.__prevX = self.__x
        self.__prevY = self.__y
    
    def move_down(self):
        if (self.__prevY - 1) >= 0:
            self.__y = self.__prevY - 1 
            
    def move_up(self):
        if (self.__prevY + 1) < 40:
            self.__y = self.__prevY + 1 
            
    def move_left(self):
        if self.__prevX - 1 >= 0:
            self.__x = self.__prevX - 1 
             
    def move_right(self):
        if self.__prevX + 1 < 40:
            self.__x = self.__prevX + 1 
    
    # Other methods
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Worker):
            return NotImplemented
        return self.__x == other.__x and self.__y == other.__y 
    
    def __repr__(self) -> str:
        return f"({self.__x}, {self.__y})"
    
    def __hash__(self) -> int:
        return hash(self.__h)
