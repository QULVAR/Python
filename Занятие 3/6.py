from random import randint as rnd

x = [rnd(1, 100) for _ in range(1, 11)]
print(x)
print(x[::-2])