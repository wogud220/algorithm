T = input()

from collections import defaultdict

for idxx in xrange(1, T+1):

	# usual input reading logic
	# SS, FF, DD : 1-indexed.
	SS = [0]
	FF = [0]
	DD = [0]

	N, TS, TF = map(int, raw_input().split())

	dp = {}

	for _ in xrange(N-1):
		s,f,d = map(int, raw_input().split())
		SS.append(s)
		FF.append(f)
		DD.append(d)

	# dp[i,j,k] = the earliest time you can reach city i after having sight-seen j cities and k = 1 means city i has been sight-seen. k = 0 otherwise.
	dp[(1, 0, 0)] = 0
	dp[(1, 1, 1)] = TS

	# iterate from city i-1 to city i.
	for n in xrange(2, N + 1):
		# consider all possible numbers of sight-seeing before reaching city y.
		for j in xrange(0, N + 1):
			# earliest leave time out of city i wihtout sight-seeing city i.
			# i.e. when the next ride (to citi i+1) comes at citi i.
			leave = None
			# earliest leave time out of city i with sight-seeing city i.
			leave2 = None

			# compute leave if there is an edge
			if (n-1, j, 0) in dp:
				t = dp[(n-1, j, 0)]
				# floor division when denom,numer are integers
				x = (t - SS[n - 1] + FF[n - 1] - 1) / FF[n - 1]
				if x < 0: x = 0
				leave = SS[n-1] + x*FF[n-1]

			# compute leave2 if there is an edge.
			if (n-1, j, 1) in dp:
				tt = dp[(n-1, j, 1)]
				xx = (tt - SS[n - 1] + FF[n - 1] - 1) / FF[n - 1]
				if xx < 0: xx = 0
				leave2 = SS[n-1] + xx*FF[n-1]

			# the case when you visit city n w/o having sight-seen at city n-1.
			if leave:

				if (n, j, 0) in dp:
					dp[(n, j, 0)] = min(dp[(n, j, 0)], leave + DD[n-1])

				elif (n, j, 0) not in dp:
					dp[(n, j, 0)] = leave + DD[n-1]
			
			# the case when you visit city with having sight-seen at city n-1.
			if leave2:
				if (n, j, 0) in dp:
					dp[(n, j, 0)] = min(dp[(n, j, 0)], leave2 + DD[n-1])
				elif (n, j, 0) not in dp:
					dp[(n, j, 0)] = leave2 + DD[n-1]

		# if it is possible to reach this city with having sight-seen j - 1 times.
		# sight-see city i to reach j times.
		# n < N: because you can't sight-see city n.
		if n < N:
			for j in xrange(1, N):
				if (n, j - 1, 0) in dp:
					if (n, j, 1) not in dp:
						dp[(n, j, 1)] = dp[(n, j - 1, 0)] + TS
					else:
						dp[(n, j, 1)] = min(dp[(n, j, 1)], dp[(n, j - 1, 0)] + TS)

	# iterate over all valid goal states.
	ans = -1
	for t in xrange(N + 1):
		if (N, t, 0) in dp and dp[(N, t, 0)] <= TF:
			ans = max(ans, t)
		elif (N, t, 1) in dp and dp[(N, t, 1)] <= TF:
			ans = max(ans, t)

	if ans == -1:
		print "Case #{0}: {1}".format(idxx, "IMPOSSIBLE")
	else:
		print "Case #{0}: {1}".format(idxx, ans)
