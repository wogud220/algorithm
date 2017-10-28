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
	
## Problem 1)
	Given a string S consisting of "(" and ")", check if the string is valid. A valid p-string is either 1) empty string, 2) "(" + p-string + ")", or 3) p-string + p-string.

	This problem can be solved using some sort of stack approach, but a DP approach is more applicable to the various variations of this problem.
	Define DP[i][j] as True if S[i:j] is a valid p-string, False otherwise. The final answer is DP[0][n-1].
	Recurrence:
	DP[i][j] = (if S[i]+S[j] = "()", DP[i+1][j-1]) or
		(DP[i][k] and DP[k+1][j] for all k = i+1, increment by 2, k<j)
	This directly follows from the recursive definition of p-strings. Either the string is enclosed by ( and ) and the inside is valid, or it is some combination of two possible p-strings. k increments by 2 because it is impossible for an odd-length p-string to be valid.
	The runtime of this algorithm is O(n^3) since for all n^2 entries, there are possibly up to O(n) operations.

## Problem 2)
	Given a p-string, find the longest valid subsequence.
	
	The solution to this problem is almost the same as problem 1.
	Define DP[i][j] as the length of the longest valid subsequence contained in S[i:j]. The final answer is DP[0][n-1].
	Recurrence:
	INC = 2 if S[i]+S[j] = "()", 0 otherwise.
	DP[i][j] = max(DP[i+1][j-1] + INC,
		(DP[i][k] + DP[k+1][j] for all k = i+1, increment by 2, k<j)).
	In a similar reasoning as problem 1, we simply go over every case of splitting the entry into smaller parts, and finding the one that gives the maximum valid subsequence.
	The runtime of this algorithm is O(n^3) since for all n^2 entries, there are possibly up to O(n) operations.

## Problem 3)
	Given a p-string, find the longest valid substring ***and its occurences***.
	
	Define DP[i] as the length of the longest valid substring starting with S[i]. The final answer is max(DP[i]).
	Recurrence:
	DP[i] = if S[i] = ")"
			0
		if S[i] = "(" and S[i+1] = ")"
			2 + DP[i+2]
		if S[i] = "(" and S[i+1] = "("
			if S[i + DP[i+1] + 1] = ")"
				2 + DP[i+1]
			else
				0
	Since DP[i] is defined to be starting at S[i], we simply need to go through every case. If S[i] is ")", then LVS is already invalid, thus the length is 0. If S[i] is "(" and S[i+1] is ")" then we can look at DP[i+2] and add two to that result. If S[i] and S[i+1] = "(", then two ")" must show up later. We find the longest occurence of this by looking at DP[i+1]. DP[i+1] tells us where the first ")" occurs, since DP[i+1] contains the length of the LVS. By summing i, this length, and 1, we are now at the index of S where the second ")" should occur, and we simply add 2 to DP[i+1]. If it does not occur, then there is no valid substring starting at S[i], thus the length is 0.
	
## Problem 4)
	Now, include [] and {} with the same constraints. Given a string containing of (){}[] and ?, find the total number of possible ways to replace the ? with one of ()[]{}. Ex) ([?) = 1, ???] = 3.
	
	The solution to this problem is almost the same as problem 1.
	Define DP[i][j] as the total number of ways to replace ? with ()[]{} in S[i:j]. The final answer is DP[0][n-1].
	Recurrence:
	INC = 3 if S[i]+S[j] = "??", 1 if S[i]+S[j] = "()", "?)", "(?". (check also for {,},[,], in similar fashion), 0 otherwise.
	DP[i][j] = max((DP[i+1][j-1] * INC),
		(DP[i][k] * DP[k+1][j] for all k = i+1, increment by 2, k<j)).
	In a similar reasoning as problem 1, we simply go over every case of splitting the entry into smaller parts, and finding the one that gives the maximum number of ways to replace ?. We multiply instead of adding like in problem 2 because we are multiplying the occurences of independent events.
	The runtime of this algorithm is O(n^3) since for all n^2 entries, there are possibly up to O(n) operations.

# Session 3. TBD.
## Problem 1)
Given a N x M grid of numbers all positive and <= 10000, you want to reach from the top left corner to the bottom right corner in the minimum number of steps. You can move from cell (i, j) to its adjacent neighbors if and only if the value of an adjacent cell is lower than that of cell (i, j).

## Problem 2)
Same problem except that you are interested in finding the number of all such paths (not necessarily minimum).

## Problem 3)
The computer memory can be conceptually thought of as an array A of N numbers. A memory cell A[i] has two values associated with it. m_i is how many bytes it represents and c_i is the cost of "free"-ing that memory cell. You want to run your favorite new game and need at least M bytes. Figure out the minimum cost sum of clearing memory cells such that you have M free bytes.

## Problem 4)
In an undirected tree (a graph that has no cycle and is connected), the diameter of a tree is defined to be the longest path between any two nodes in a tree. Give a recurrence relation that computes the diameter of a tree.
