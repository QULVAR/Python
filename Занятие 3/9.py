x = list(map(int, input().split()))
a = int(input())
maxi = x[:a]
for i in range(1, len(x) - a + 1):
	maxi = max(maxi, sum(x[i: i + a]))
print(maxi)