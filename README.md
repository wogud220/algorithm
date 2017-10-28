# COMP 382 training

This repoistory serves as a place for consolidating 1) problems we went over in each session 2) our analysis for each problem and 3) each person's implementations for some or all of the problems.

# Session 1. 10.26.17'

## Problem 1)
	Given a set of x coordinates x1, x2, ..., xn and some rewards associated with each coordinate r1, r2, ..., rn, find the subset of x coordinates such that x_(i+1) - x_i >= 5 and the sum of corresponding r_i for each element in the subset is maximized.

	Approach 1)
		TODO: fill this out

	Approach 2)
		TODO: fill this out
	
	Approach 3)
		TODO: fill this out

## Problem 2)
	Same problem as Problem 1 with the added constraint that the subset has to be exactly of some given size K.

## Problem 3)
	Same problem as problem 2 except that the the subset can be of size upto some given size K.	

# Session 2. 10.27.17'
	
	TODO: update me.

# Session 3. TBD.
## Problem 1)
Given a N x M grid of numbers all positive and <= 10000, you want to reach from the top left corner to the bottom right corner in the minimum number of steps. You can move from cell (i, j) to its adjacent neighbors if and only if the value of an adjacent cell is lower than that of cell (i, j).

## Problem 2)
Same problem except that you are interested in finding the number of all such paths (not necessarily minimum).

## Problem 3)
The computer memory can be conceptually thought of as an array A of N numbers. A memory cell A[i] has two values associated with it. m_i is how many bytes it represents and c_i is the cost of "free"-ing that memory cell. You want to run your favorite new game and need at least M bytes. Figure out the minimum cost sum of clearing memory cells such that you have M free bytes.

## Problem 4)
In an undirected tree (a graph that has no cycle and is connected), the diameter of a tree is defined to be the longest path between any two nodes in a tree. Give a recurrence relation that computes the diameter of a tree.
