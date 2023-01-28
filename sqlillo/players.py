from __future__ import annotations
from typing import List, Callable, Tuple, Iterable
from .constants import WORKERCOLORS
from .player import Player
from random import shuffle

class Players:

    __slots__ = 'players', 'strategies'

    def __init__(self, strategies: List[Tuple[str, Callable]]):
        self.strategies = strategies
        self.players: List[Player] = list()
        self._init()

    def _init(self):
        self.players.clear()
        # randomly assign colors to every player
        shuffle(WORKERCOLORS)
        for color, strategy in zip(WORKERCOLORS, self.strategies):
            self.players.append(Player(strategy, color))

    def getPlayersWorkers(self) -> List[Worker]: 
        ll = list() # type: ignore
        for player in self.players:
            ll += player.workers

        return ll

    def validate(self):
        allWorkers = self.getPlayersWorkers()
        n = 0

        while n != len(allWorkers):
            POIs = dict()
            for w in allWorkers:
                p = (w.x, w.y)
                if p in POIs:
                    POIs[p].append(w)
                else:
                    POIs[p] = [w]

            for poi in POIs:
                if len(POIs[poi]) > 1:
                    for w in POIs[poi]:
                        w._invalidate()

            n = len(POIs)

        for w in allWorkers: 
            w._validate()

    def play(self, mapa: Board): 
        for player in self.players:
            player.play(mapa)

        self.validate()