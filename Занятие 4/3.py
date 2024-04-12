s = set()
for i in list(map(int, input().split())):
	print('YES' if i in s else 'NO')
	s.add(i)
