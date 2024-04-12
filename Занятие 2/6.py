a = int(input()) - 1
N = '1'
for _ in range(a):
	newN = ''
	k = 1
	if len(N) > 1:
		for i in range(1, len(N)):
			if N[i-1] == N[i]:
				k += 1
			else:
				newN += f'{k}{N[i-1]}'
				k = 1
		newN += f'{k}{N[i]}'
	else:
		newN = '11'
	N = newN
print(N)