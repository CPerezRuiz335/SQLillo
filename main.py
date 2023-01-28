from __future__ import annotations
import pygame # type: ignore
import sys
# Player modules
from typing import *
from collections import *
from random import *
from math import *
# --------------
from sqlillo import RED, YELLOW, BLUE, GREEN, EMPTY, ANY, VALIDMOVES
from sqlillo import WIDTH, HEIGHT, Game, Strategy

# Parse 
strategies = list()
args: Dict[str, Callable] = dict()

for f in sys.argv[1:]:
    with open(f"./strategies/{f}") as ff:
        exec(ff.read(), globals(), args)
        strategies.append(Strategy(f.removesuffix('.py'), args['strategy']))

if not strategies:
    with open(f"./strategies/random.py") as ff:
        exec(ff.read(), globals(), args)
        strategies = [Strategy('random', args['strategy']) for _ in range(4)]

# Main 
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('SQLillo')

def main():
    FPS = 60; clock = pygame.time.Clock()
    run = True; stop  = False 
    game = Game(maxticks = 500, WIN = WIN, strategies = strategies)
    
    while run:
        clock.tick(FPS)
        
        if not stop:
            pygame.event.clear()
            game.play()
        
        # Controls
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
            FPS = 25
            stop = True
            
            if pressed[pygame.K_LEFT]:
                game.backward()
            else:
                game.forward()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    FPS = 60
                    stop = not stop

                if event.key == pygame.K_c:
                    stop = True
                    game.new_game()                    
                
                if event.key == pygame.K_q:
                    run = False

        pygame.display.update()

    pygame.quit()
        
main()        

