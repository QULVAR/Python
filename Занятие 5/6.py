s = input().split()
num = int(s[0])
i = 1
while i < len(s)-1:
	num1 = s[i]
	chr = s[i+1]
	num = eval(f'{num} {chr} {num1}')
	i += 2
print(num)