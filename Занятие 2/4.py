s = input()
s = s.strip(' ')
s = s.replace(',', ', ')
s = s.replace('.', '. ')
while '  ' in s:
	s = s.replace('  ', ' ', 1)
s = s.replace(' ,', ', ')
s = s.replace(' .', '. ')
print(s)