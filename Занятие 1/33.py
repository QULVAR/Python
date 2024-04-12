nn = 1
k = 0
for i in range(1, int(input()) + 1):
	nn *= i
	k += nn
print(k)