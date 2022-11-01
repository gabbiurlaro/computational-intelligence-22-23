# Lab2: Set covering using Genetic Algorithm

The main idea of this algorithm is the way we represent the individual. We start by transformign the list of list in a list of tuple, and removing the duplicated element, to avoid inserting twice an element.

```python
all_states = list(set([tuple(x) for x in problem(5, seed=42)]))
```

The genome is a bitmap(same size of `all_states`):

- 1 means that the corresponding tuple has been picked in the solution
- 0 none.

The genome is encapsuleted in a Individual class.

### Fitness function
