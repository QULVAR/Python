def f():
	if len(s) % 2:
		print(len(s) // 2 + 1)
	else:
		print(len(s) - 1)

s = input()
if s == s[::-1]:
	print(0)
else:
	if s.index(s[-1]) + 1 != len(s):
		flag = True
		k = 1
		while True:
			i = s.index(s[-1], k)
			j = len(s) - 1
			flag1 = True
			if i == j:
				f()
				break
			while i < len(s):
				if s[i] == s[j]:
					i += 1
					j -= 1
				else:
					flag1 = False
					break
			if flag1:
				print(s.index(s[-1], k))
				flag = False
				break
			else:
				k += 1
	else:
		f()