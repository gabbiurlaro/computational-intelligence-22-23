# Lab2: Set covering using Genetic Algorithm

The main idea of this algorithm is the way we represent the individual. We start by transformign the list of list in a list of tuple, and removing the duplicated element, to avoid inserting twice an element.

```python
all_states = list(set([tuple(x) for x in problem(5, seed=42)]))
```

### Representation

The usual bit-representation is straightforward for this problem:

- 1 means that the corresponding tuple(or list) has been picked in the solution
- 0 none.

The genome is encapsuleted in a `Individual` class, together with his fitness. To compute fitness every Individual class has a reference to the problem.

### Fitness function

### Genetic algorithm

I decided to implement a solution called _steady-state_[1], which mean that the offspring does not completely replace the population and the generation goes until a satisfactory solution is reached.

### References

[1] [A genetic algorithm for the set covering problem](https://reader.elsevier.com/reader/sd/pii/037722179500159X?token=78C4D65C25B633E43DE06B0707227F5C0B6A2B802A822088598CE4D2F63E3FCA9C8AE9113276FEC4996AAA804F38D099&originRegion=eu-west-1&originCreation=20221102071947) J.E. Beasley, RC. Chu, The ManagementSchool, Imperial College,London SW7 2AZ, UK
