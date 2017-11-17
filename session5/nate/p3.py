# refer to https://www.evernote.com/shard/s726/sh/bc3c9ae3-55d3-4775-bb2b-a00307ff9742/b2a9f6e26d2259bed0227e7348c8504b

def bsearch_left(A, x):
	lo = -1
	hi = len(A)  # n
	# invariants
	# 1) answer lies in (lo, hi]
	# N N N N N N N Y Y Y Y Y Y
	#              (^)
	# 2) lo < hi
	# 3) the answer must be 'hi'
	while lo + 1 < hi:
		mid = (lo + hi) / 2
		if A[mid] >= x:
			hi = mid
		else:
			lo = mid
	return hi

def bsearch_right(A, x):
	lo = -1
	hi = len(A)  # n
	# invariants
	# 1) answer lies in [lo, hi)
	# Y Y Y Y Y Y Y N N N N N N
	# 2) lo < hi
	# 3) the answer must be 'lo'
	while lo + 1 < hi:
		mid = (lo + hi) / 2
		if A[mid] <= x:
			lo = mid
		else:
			hi = mid
	return lo

A = [2, 3, 3, 3, 4, 7]

print 'result for bsearch_left.'
for x in xrange(0, 9):
	print x, bsearch_left(A, x)

print 'result for bsesarch_right.'
for x in xrange(0, 9):
	print x, bsearch_right(A, x)

 
