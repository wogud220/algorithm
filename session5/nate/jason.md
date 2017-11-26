# Session 5
## Problem 1)
Given a directed graph with N nodes and E edges where there is no negative sum cycle, you want to find the shortest path from node S to node T. To make the problem interesting, consider a set of one way flights F that connect you from node s_i to node e_i for each flight i and you can ride at most one flight. Find the shortest path from node S to node T that may include at most one such flight. Note that the number of N, E <= 10^6. You want to design an algorithm that runs under 1s and a modern machine can process about O(10^8) operations in 1s.

This problem can be solved using the same technique used to find the second shortest path between two nodes. Run Dijkstra's algorithm from node S to find the shortest distance to every other node. Run it on node T as well, with the edges reversed. Now, iterate through every element in the set of flights, and sum the paths on either side. Doing this gives us the cost of the path from S to T using one flight. Finally, we should also compare to the cost of going from S to T without using any flight, since that may actually be faster.

## Problem 2)
Given a directed graph with N nodes and E edges, you have a robot that starts at some node S. The robot has one pre-programed rule, which dictates it to always take a certain directed edge e_i (other than some other directed edges) when it is at some node n_i. Additionally, some nodes count for destinations where the robot may stop. This robot unfortunately is buggy and can make upto 1 mistake of violating the rule. Find the number of distinct destinations the robot may end up at.

TODO

## Problem 3)
Binary Search

Key takeaways:
a. Define the point in the sequence we want to find (when the predicates turn from YYYNNN or NNNYYY)
b. Define loop invariants - answer range, parameter constraints.
c. In the loop, make sure not to break invariants. Also make sure that progress is being made on each loop (will terminate)
d. There should be a clear answer to return once the parameter constraints are no longer met.

## Auxilliary Problem Notes
Given your position in a line, determine which server will serve you

Monotonic Nature: Given time T, will I have been served?
-> Will look like NNNNNYYYYY
-> Use BinSearch to find first point at which answer is Y
-> Use modulo to easily find server
