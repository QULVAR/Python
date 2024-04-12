a = int(input())
b = int(input())
c = (a // 2 + a % 2) * 2
print([ i for i in range(c, b + 1, 2)])