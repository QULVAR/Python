s = input().split()
d = dict.fromkeys(s, 0)
for i in s:
	print(d[i], end = ' ')
	d[i] += 1