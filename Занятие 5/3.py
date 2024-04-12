n = int(input())
d = {}
for i in range(n):
	s = input().split()
	d[s[0]] = s[1]
s = input()
dv = list(d.values())
dk = list(d.keys())
if s in dv:
	print(dk[dv.index(s)])
else:
	print(dv[dk.index(s)])