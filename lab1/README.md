## Lab 1: set Covering

Gabriele Iurlaro - Salvatore Adalberto Esposito

The main file solution is set_covering.ipynb. The main idea is to use A\* algorithm, using as heuristic the number of element that we haven't covered yet. It's possible to implement also a limitation of the branching factor passing a max argument to possibile action.

We have observed that A\* does not provide us a solution in a reasonable amount of time(for N greater 20),so we moved to a greedy best-first solution, using the same heuristic of the previous case.

### Heuristic

The heuristics is very simple, and has a simple interpretation. Given $u(n)$ the number of element covered by a given state, $h(n) = N -u(n)$ is the number of element not yet covered. Intuitively, the heuristic is admissible, because it never overestimate the minor cost. That's because, if we have to cover 2 element to solve the problem, the best solution is to find a list of 2 elements that contains exactly the 2 elements.

### Experimental result

A\* provides the following results:
| N | W | bloat |
|---|---|-------|
| 5 | 5 | 0 |
| 10| 10| 0 |
| 20| 24| 20 |
