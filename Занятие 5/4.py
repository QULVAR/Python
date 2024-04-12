n = int(input())
d = {}
for i in range(n):
	s = input().split()
	d[s[0]] = s[1]
ds = sorted(d.items(), key=lambda g: g[1])
print()
for i in ds:
	print(i[0], i[1])