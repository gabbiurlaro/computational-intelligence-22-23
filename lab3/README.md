# Lab 3 - Nim

In group with Salvatore Adalberto Esposito - 304800

### Task 3.1

The main idea of the hardcoded strategy is that we cannot do always the same thing for the entire duration of the game. Like chess, that is divided in opening, middle game and end game, we can divide Nim in 2 phases:

- Early game: in this phase, we try to remove the most from the row, but we will try to keep always a stick in it
- Late game: in this phase, we will take all from the row, to finish the game early

The distinction is base on the completation, computed as the number of stick remaining on the boar divided by the total number of sticks.

### Task 3.2

We evolved two strategies:

- `evolvable_strategies` is the one mentioned before, the parameter to evolve are:
  - `max_k`: a maximum amout of sticks
  - `turn_strategies`: when we turn strategies
- `evolvable_random_strategies`: since the one before plays always the same, we introduced a bit of randomness in the play, resulting in slightly better result.
