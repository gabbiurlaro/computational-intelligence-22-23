# Lab 3 - Nim

In group with Salvatore Adalberto Esposito - 304800

## Task 3.1 - hardcoded

The main idea of the hardcoded strategy is that we cannot do always the same thing for the entire duration of the game. Like chess, that is divided in opening, middle game and end game, we can divide Nim in 2 phases:

- Early game: in this phase, we try to remove the most from the row, but we will try to keep always a stick in it
- Late game: in this phase, we will take all from the row, to finish the game early

The distinction is base on the completation, computed as the number of stick remaining on the boar divided by the total number of sticks.

The other strategies is based on a simple assumption: if it's my turn i can easily remove one row(if k is `None`), and this is useful only if there are odd rows active. We called it aggressive, and it's a variant of `gabriele`.

The `aggressive` strategies seems to be very effective against the other one, results are reported in this table:

|                 | gabriele | pure random | aggressive | Optimal |
| --------------- | -------- | ----------- | ---------- | ------- |
| **gabriele**    | 1.0      | 0.81        | 0.0        | 0.0     |
| **pure random** | 0.17     | 0.54        | 0.18       | 0.0     |
| **aggressive**  | 1.0      | 0.76        | 0.48       | 0.0     |
| **Optimal**     | 1.0      | 1.0         | 1.0        | 1.0     |

## Task 3.2 - evolved rules

We evolved two strategies:

- `evolvable_strategy` is the one mentioned before, the parameter to evolve are:
  - `max_k`: a maximum amout of sticks
  - `turn_strategies`: when we turn strategies
- `evolvable_random_strategy`: since the one before plays always the same, we introduced a bit of randomness in the play, resulting in slightly better result.

There was the idea to embed some kind of aggressive strategy in the evolved one, but we had the idea too late and it was difficult. In the next days we will provide an implementation.
Our idea is to have a lot of players for a future use.

## Task 3.3 - minmax

We implemented a simple recursive algorithm for min-max, that was able to win against the optimal strategy, but only for small cases. Without a limit in the depth, it was unfeasible to use it, also with alpha-beta pruning.

## Task 3.4 - reinforcement learning

During this journey in trying to implement a Reinforcement learning agent to play Nim, we have explored several ideas:

- Learn directly a value for the state and choose the action that lead to this state(:-1:)
- Learn the Q table (:boom:)

Since with the first approach we wasn't able to achieve good result, we moved on the second one.

### Reinforcement learning details

First when initializing the player, we generate all possible $(s, a)$ pair(with $ s \in S, a \in A$), with a very simple recursive algorithm. The recursion is also our main bottleneck, and we are not able to play Nim bigger then 8(For exmaple, for `NIM_SIZE = 7`, we generate `4404719` pairs in 3 minutes).

We concentrate our analysis in learn to win against the `optimal_strategy`. We have found that the agent, if learns only to win against it, can learn also to win against the other strategy we have used before.

