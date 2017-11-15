# Session 3
## Problem 1)
Given a N x M grid of numbers all positive and <= 10000, you want to reach from the top left corner to the bottom right corner in the minimum number of steps. You can move from cell (i, j) to its adjacent neighbors if and only if the value of an adjacent cell is lower than that of cell (i, j).

When we look at a point i,j on the grid, we are required to either parse through the rest of the graph or have the solution to some subproblem. Thus, this problem probably requires a DP solution.
DP[i][j] = The minimum number of steps it takes from A[i][j] to A[N-1][M-1].
Answer : DP[0][0]

DP[i][j] = min(DP[i-1][j] if A[i-1][j] < A[i][j],
DP[i][j-1] if A[i][j-1] < A[i][j],
DP[i+1][j] if A[i+1][j] < A[i][j],
DP[i][j+1] if A[i][j+1] < A[i][j]) + 1
Base Cases to consider: If i=n-1, j=m-1. Possible other cases depending on implementation.

Check all four directions, check if you can move there (lower cell value), and find the minimum, add one (because you are taking a step)
This definitely ends, because the lower value constraint means you will never traverse back onto a path that you already have.
Runtime is O(NM), at max you will fill out the entire DP table, with each iteration doing constant number of operations.
This is definitely a DP you want to do top-down (which I need to learn).

## Problem 2)
Same problem except that you are interested in finding the number of all such paths (not necessarily minimum).

This can be saved in almost the same way.
DP[i][j] = The number of paths you can go from A[i][j] to A[N][M].
Answer : DP[0][0]

DP[i][j] = sum(DP[i-1][j] if A[i-1][j] < A[i][j],
DP[i][j-1] if A[i][j-1] < A[i][j],
DP[i+1][j] if A[i+1][j] < A[i][j],
DP[i][j+1] if A[i][j+1] < A[i][j])

## Problem 3)
The computer memory can be conceptually thought of as an array A of N numbers. A memory cell A[i] has two values associated with it. m_i is how many bytes it represents and c_i is the cost of "free"-ing that memory cell. You want to run your favorite new game and need at least M bytes. Figure out the minimum cost sum of clearing memory cells such that you have M free bytes.

I believe this problem is an extension of the Knapsack problem.

DP[i][j] = Minimum cost of clearing at least j bytes using some combination of A[0] to A[i].
Answer: DP[N-1][M]

DP[i][j] = min(DP[i-1][j],
DP[i-1][j-m_i] + c_i
Base Cases to consider: When m_i is greater than or equal to j, DP[i][j] = c_i

The intuition is that when you are looking at up to the ith cell, there are only two options:
1) DO NOT use the ith cell. Then, the problem is as if the ith cell does not exist. Simply look at DP[i-1][j] to find your value
2) DO use the ith cell. Then, you have freed up m_i bytes. Thus, look at the best you can do using up to the i-1th cell, with j minus m_i bytes still needing to be cleared. We add c_i afterwards, since that is the cost of freeing cell i.

This algorithm runs in O(NM). The table is that size, which constant operations for each iteration.
Note that like the knapsack problem, this is pseudo-polynomial, since the input size is not M, it is logM (bytes needed to represent number M)


## Problem 4)
In an undirected tree (a graph that has no cycle and is connected), the diameter of a tree is defined to be the longest path between any two nodes in a tree. Give a recurrence relation that computes the diameter of a tree.

The diameter of any given tree is one of two things:
1) The maximum diameter of either its left or right child.
2) The maximum depth of left child + maxdepth right child + 1(the node itself)
A simple diagram showcases that this are the only two possibililities.

Depth(Tree) = max(maxDepth(left) + maxDepth(right) + 1),
Depth(Left),
Depth(Right))

TODO: Implementation.


