from collections import namedtuple, Counter
import random
from itertools import accumulate
from operator import xor
import numpy as np
from copy import deepcopy, copy

Nimply = namedtuple("Nimply", "row, num_objects")

class Nim:
    def __init__(self, num_rows: int, k: int = None, state = None) -> None:
        self.size = num_rows
        if state:
            self._rows = state
        else:
            self._rows = [i * 2 + 1 for i in range(num_rows)]
            self._k = k
            self._sticks = sum(self._rows)

    def __bool__(self):
        return sum(self._rows) > 0

    def __str__(self):
        return "<" + " ".join(str(_) for _ in self._rows) + ">"

    def __eq__(self, __o: object) -> bool:
        # return self._sticks == __o._sticks
        c = Counter(self._rows)
        del c[0]       
        c1 = Counter(__o._rows)
        del c1[0]
        return c == c1
        
    def __hash__(self) -> int:
        c = Counter(self._rows)
        del c[0]
        return hash(c.__str__())
        
    @property
    def rows(self) -> tuple:
        return tuple(self._rows)

    @property
    def k(self) -> int:
        return self._k

    @property
    def sticks(self) -> int:
        return self._sticks

    def nimming(self, ply: Nimply) -> None:
        row, num_objects = ply
        assert self._rows[row] >= num_objects
        assert self._k is None or num_objects <= self._k
        self._rows[row] -= num_objects

    # -1 if I don't win, 0 if I make the last winnning move
    def give_reward(self) -> int:
        return -1 * int(self.__bool__())

    def get_state_and_reward(self):
        return self, self.give_reward()

    def possible_moves(self): 
        return [(r, o) for r, c in enumerate(self.rows) for o in range(1, c + 1)]
         
def nim_sum(state: Nim) -> int:
    *_, result = accumulate(state.rows, xor)
    return result

def cook_status(state: Nim, complete=False) -> dict:
    cooked = dict()
    cooked["possible_moves"] = [
        (r, o) for r, c in enumerate(state.rows) for o in range(1, c + 1) if state.k is None or o <= state.k
    ]
    cooked["active_rows_number"] = sum(o > 0 for o in state.rows)
    cooked["shortest_row"] = min((x for x in enumerate(state.rows) if x[1] > 0), key=lambda y: y[1])[0]
    cooked["longest_row"] = max((x for x in enumerate(state.rows)), key=lambda y: y[1])[0]
    cooked["completation"] = sum(state.rows)/state.sticks
    if complete:
        brute_force = list()
        cooked["nim_sum"] = nim_sum(state)
        for m in cooked["possible_moves"]:
            tmp = deepcopy(state)
            tmp.nimming(m)
            brute_force.append((m, nim_sum(tmp)))
        cooked["brute_force"] = brute_force
    return cooked

def optimal_strategy(state: Nim) -> Nimply:
    data = cook_status(state, complete = True)
    return next((bf for bf in data["brute_force"] if bf[1] == 0), random.choice(data["brute_force"]))[0]

def aggressive(state: Nim) -> Nimply:
    """Pick always the entire row if the number of active rows is odd"""
    data = cook_status(state)
    if data['active_rows_number'] % 2 == 0:
        # random move
        row, num_objects = random.choice(data['possible_moves'])
    else:
        # aggressive move
        row = data['longest_row']
        num_objects = state.rows[row]
    return Nimply(row, num_objects)

def pure_random(state: Nim) -> Nimply:
    row = random.choice([r for r, c in enumerate(state.rows) if c > 0])
    num_objects = random.randint(1, state.rows[row])
    return Nimply(row, num_objects)