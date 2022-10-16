### Lab 1: set Covering

Gabriele Iurlaro - Salvatore Adalberto Esposito

The main file solution is set_covering.ipynb. The main idea is to use A\* algorithm, using as heuristic the number of element that we haven't covered yet. It's possible to implement also a limitation of the branching factor passing a max argument to possibile action.

We have observed that A\* does not provide us a solution in a reasonable amount of time, s we moved to a greedy best-first solution, using the same heuristic of the previous case.
