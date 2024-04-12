n, k = map(int, input().split())
x = []
alll = set()
for i in range(k):
	d1, d2 = list(map(int, input().split()))
	s = set()
	while d1 <= n:
		s.add(d1)
		d1 += d2
	alll = alll.union(s)
weekends = set()
i = 7
while i <= n:
	weekends.add(i - 1)
	weekends.add(i)
	i += 7
alll.difference_update(weekends)
print(alll)