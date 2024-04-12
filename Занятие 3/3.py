from random import randint as rnd

k = 0
x = [rnd(1, 100) for _ in range(1, 11)]
print(x)
for i in range(1, len(x) - 1):
	if x[i-1] < x[i] and x[i] > x[i + 1]:
		k += 1
print(k)