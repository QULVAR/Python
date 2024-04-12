s = input()
s = s.lower()
f = True
i = 0
j = len(s) - 1
while i < len(s):
	ci = ord(s[i])
	if ci < 97 and 122 > ci:
		i += 1
		continue
	cj = ord(s[j])
	if cj < 97 and 122 > cj:
		j -= 1
		continue
	f = ci == cj
	i += 1
	j -= 1
	if not(f):
		break
print(f)