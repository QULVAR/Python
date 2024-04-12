table = str.maketrans('0123456789', '5987604321')
s = input()
print(s.translate(table))