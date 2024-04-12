from random import randint as rnd

x = [rnd(1, 100) for _ in range(1, 11)]
print(x)
maxi = max(x)
mini = min(x)
x[x.index(maxi)] = mini
x[x.index(mini)] = maxi
print(x)