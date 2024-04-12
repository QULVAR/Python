n = int(input())
call = set()
cone = set()
for i in range(n):
	s = set(map(int, input().split()))
	call = s if call == set() else call.intersection(s)
	cone = cone.union(x[i])
print('all, ', call)
print('one, ', cone)