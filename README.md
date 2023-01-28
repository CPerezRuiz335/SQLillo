
<h1 align="center"> SQLillo </h1>

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-v3.10+-blue.svg">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/CPerezRuiz335/SQLillo?color=informational">

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

When the game is over the winner becomes the player with biggest connected component!  
</p>
  
_Adapted from https://sqlillo.com/  (no longer working)_

Contents
---------

* [Rules](#rules)
* [Strategy](#strategy)
* [Usage](#usage)

## Rules

+ Each worker has to be in a unique position.

## Strategy

#### Worker
#### Mapa
#### Memory
#### Random

## Usage



