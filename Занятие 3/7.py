x = list(map(int, input().split()))
print(sorted(x, key= lambda g: x.count(g), reverse=True)[0])