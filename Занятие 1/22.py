n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n < m:
	_ = n
	n = m
	m = _
x = n - x if x > n - x else x
y = m - y if y > y - m else y
print(y if x > y else x)