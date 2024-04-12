x = list(map(int, input().split()))
s = 0
k = 0
for i in range(0, len(x) - 1):
	if x[i] == 2 and x[i + 1] != 2:
		pass
	else:
		s += x[i]
		k += 1
s += x[-1]
k += 1
arif = s / k
print(int(arif))
