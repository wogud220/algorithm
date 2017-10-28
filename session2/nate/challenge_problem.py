def solve(start, end):
	# If (start, end) is a state which already has been computed, return its value
	if (start, end) in dp:
		return dp[(start, end)]
	# A subarray of length 1 is never valid.
	if start == end: return 0
	# An empty subarray is valid.
	if start > end: return 1
	# A subarray of odd length is never valid.
	if (end - start + 1) % 2 == 1: return 0

	res = 0
	# If the current character is (, {, or [, you try segmenting the [start, end] in all valid ways
	# and the count is (# of valid ways in the first half) * (# of valid ways in the 2nd half).
	# If the current charcater is ?, identical logic except that if the matching character is also a ? character
	# then you multiply 3 * the result. 3 because a pair of (?, ?) can be (, ) or [, ] or {, }
	if s[start] == '(':
		for idx in xrange(start + 1, end + 1, 2):
			if s[idx] == ')' or s[idx] == '?':
				solve_rest = (solve(start + 1, idx - 1) * solve(idx+1, end))
				res += solve_rest
	elif (s[start] == '{'):
		for idx in xrange(start + 1, end + 1, 2):
			if s[idx] == '}' or s[idx] == '?':
				solve_rest = (solve(start + 1, idx - 1) * solve(idx+1, end))
				res += solve_rest
	elif (s[start] == '['):
		for idx in xrange(start + 1, end + 1, 2):
			if s[idx] == ']' or s[idx] == '?':
				solve_rest = (solve(start + 1, idx - 1) * solve(idx+1, end))
				res += solve_rest
	elif s[start] == '?':
		for idx in xrange(start + 1, end + 1, 2):
			if s[idx] == '?':
				solve_rest = (3 * solve(start + 1, idx - 1) * solve(idx+1, end))
				res += solve_rest
			elif s[idx] == ')' or s[idx] == '}' or s[idx] == ']':
				solve_rest = (solve(start + 1, idx - 1) * solve(idx+1, end))
				res += solve_rest
	dp[(start, end)] = res
	return res

n = input()
s = raw_input().strip()
dp = {}
print str(solve(0, n - 1))[-5:]