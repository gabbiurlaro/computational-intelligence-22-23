# Lab2: Set covering using Genetic Algorithm

The main idea of this algorithm is the way we represent the individual. We start by transforming the list of list in a list of tuple, and removing the duplicated element, to avoid inserting one twice:

```python
all_states = list(set([tuple(x) for x in problem(5, seed=42)]))
```

### Representation

The usual bit-representation is straightforward for this problem:

- 1 means that the corresponding tuple(or list) has been picked in the solution
- 0 none.

The genome is encapsuleted in a `Individual` class, together with his fitness. To compute fitness every Individual class has a reference to the problem. The fitness is computed once for every individual at "creation time", to avoid inefficiencies.

### Fitness function

Our goal is to cover all the numbers with lists of minimum size. So I've decided to implement the fitenss as a tuple: $$f = (covered, -\sum_{s \in S} len(s))$$
Where covered is the number of item covered by the solution. I've tried different combination of this parameter, also a weighted sum of this contributes plus a bonus if they reach the solution, but this ones converges to a solution pretty fast.

### Genetic algorithm

I decided to implement a solution that use _steady-state_ as terminating condition, which mean that the offspring does not completely replace the population and the generation goes until a satisfactory solution is reached(or when we reach the maximum number of iterations).

The steady state is implemented using a `deque`(used as circular buffer), and at every generation we check that the fitness has not get an improvement in the last `STEADY_STATE_COUNT_SOLUTION`.

### Results

Then, we discuss a little bit the obtained result. For every problem, the number of generation required to reach the plateau is little(below 100).

| N    | w    | bloat(%) | generation |
| ---- | ---- | -------- | ---------- |
| 5    | 5    | 0        | 23         |
| 10   | 10   | 0        | 55         |
| 20   | 29   | 45       | 34         |
| 100  | 216  | 116      | 41         |
| 500  | 1557 | 211.4    | 61         |
| 1000 | 3757 | 275.7    | 63         |
