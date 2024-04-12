n = int(input())
d = {}
for i in range(n):
	s = input().split()
	d.update(dict.fromkeys(s[1:], s[0]))
print()
n = int(input())
cities = []
for i in range(n):
	cities.append(input())
print()
for i in cities:
	print(d[i])