T = input()

from collections import defaultdict

for idxx in xrange(1, T+1):
	SS = [0]
	FF = [0]
	DD = [0]

	N, TS, TF = map(int, raw_input().split())
	dp = defaultdict(int)
	dp2 = []
	for i in xrange(N+1):
		dp2.append(set())

	for _ in xrange(N-1):
		s,f,d = map(int, raw_input().split())
		SS.append(s)
		FF.append(f)
		DD.append(d)
	dp[(1, 0)] = 0
	dp2[1].add(0)
	for n in xrange(1, N):
		for t in dp2[n]:
			x = (t - SS[n] + FF[n] - 1) / FF[n]
			if x < 0: x = 0
			xx = (t + TS - SS[n] + FF[n] - 1) / FF[n]
			if xx < 0: xx = 0
			leave = SS[n] + x*FF[n]
			leave2 = SS[n] + xx*FF[n]
			if leave + DD[n] <= TF:
				dp[(n+1,leave + DD[n])] = max(dp[(n+1,leave + DD[n])], dp[(n, t)])
				dp2[n+1].add(leave + DD[n])
			if leave2 + DD[n]<= TF:
				dp[(n+1,leave2 + DD[n])] = max(dp[(n+1,leave2 + DD[n])], dp[(n, t)] + 1)
				dp2[n+1].add(leave2 + DD[n])

	ans = -1
	for t in dp2[N]:
		ans = max(ans, dp[(N,t)])
	if ans == -1:
		print "Case #{0}: {1}".format(idxx, "IMPOSSIBLE")
	else:
		print "Case #{0}: {1}".format(idxx, ans)
