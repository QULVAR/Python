s = sorted(input().split())
d = {n: s.count(n) for n in s}
dsotred = sorted(d.items(), key=lambda g: g[1], reverse=True)
print(dsotred[0][0])