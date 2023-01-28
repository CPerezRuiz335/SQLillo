
<h1 align="center"> SQLillo </h1>

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-v3.10+-blue.svg">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/CPerezRuiz335/SQLillo">

 </div>
 
<p align="center">
  <img src="media/output.gif" alt="animated" />
</p>

<p align="justify"> 
There is a map you can imagine as an N-dimensional canvas of 40x40. 
The map has only integer positions like [1, 2]. No decimals allowed! 
We will use a Cartesian coordinate system, where the bottom left corner
corresponds to the origin, and the top right corner is [39, 39] coordinate. 
You (a player) are assigned a unique color and a set of what we call a <i>worker</i>.

Each <i>worker</i> has a palette of your unique team color and can paint the map. 
However, it can only move row or column-wise, just like a rook in chess but one square 
at a time. But beware, there are also more players on the map!

The challenge will be as follows. Every X unit of time there will be an iteration of 
the game, named a tick. On each tick, each player decides where his <i>workers</i> should go, and
on the next tick, if there are no collisions (see the rules section for more details), each
<i>worker</i> will be placed in the defined position. When a <i>worker</i> moves to its desired position, 
it paints its path with a softer tonality than your team's color. Therefore, 
after a few ticks, the map will be a beautiful and colorful canvas with the colors of the players. 

When the game is over the winner becomes the player with the biggest connected component!  
</p>
  
_Adapted and inspired by https://sqlillo.com/  (no longer working)_

Contents
---------

* [Rules](#rules)
* [Strategy](#strategy)
* [Usage](#usage)

## Rules

+ Two or more workers in the same coordinate are not allowed.
  * They will be invalidated and their positions will be the same as the previous tick.\
    However, two adjacent workers can swap positions because this rule is not violated 
    on the next tick.
+ Workers can not overrun edges and appear on the opposite side.
+ Each game lasts 500 ticks, but you can change that in main.py line 34.
+ Connected components are not evaluated considering diagonal adjacencies.
+ Have fun.

## Strategy

Your strategy has to be defined in a unique file without imports, if you want to import some 
fancy import it in the main.py file. There you can control which libraries are available 
for each player. Strategies that involve multiple files are not tested and everything must
be inside the function strategy.

```
# strategies/random.py
def strategy(mapa: Board, worker: Tuple[Worker], memory: Dict[Any, Any]) -> None:
    for w in range(8):
        r = randint(0, 3)
        match r:
            case 0:
                worker[w].move_up()
            case 1:
                worker[w].move_down()
            case 2:
                worker[w].move_left()
            case 3:
                worker[w].move_right()
```

#### Worker

Each player has a tuple of 8 workers that do not change positions between ticks (you can control everyone
by its position in the tuple). You control every worker with four methods and everyone has its x and y position,
and its team color (BLUE, YELLOW, GREEN, RED) which are predefined constants. VALIDMOVES and ANY are also available 
constants for every player.

```
VALIDMOVES = [[-1,0], [1,0], [0,-1], [0,1]]
ANY = [RED, YELLOW, BLUE, GREEN, EMPTY]

worker[w].x
worker[w].y
worker[w].color

# Initial positions and indexes for worker
0 3 5
1   6
2 4 7
```

If a player moves multiple times the same worker only the last movement will be considered!

#### Mapa

Each player has a copy of the board which contains a tuple of copies of all workers on the board. 
In addition you can check the color of every coordinate.

```
mapa.workers
mapa[x, y] -> BLUE, YELLOW, GREEN, RED, EMPTY
```

#### Memory

This is a dictionary where you can save whatever you want. Everything you put inside is not lost between ticks.

## Usage

If no strategy is supplied four random players are displayed. You can make 1 up to 4 strategies compete against each other.
main.py looks up strategies folder so if you create one you have to put your file inside strategies.

```sh
python3 main.py STRATEGY STRATEGY STRATEGY STRATEGY

# demo gif
python3 main.py bfs.py random.py random.py random.py
```

#### Controls

| | |
|-------|-------------------------|
| **C**     | New game              |
| **SPACE** | Stop/Play game          |
|**←**      | Stop & replay backwards |
| **→**     | Stop & replay forwards  |
| **Q**     | Quit                    |



