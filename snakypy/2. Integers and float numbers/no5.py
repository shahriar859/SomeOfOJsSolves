import math
a = float(input())
f = math.modf(a)
g = str(f[0])
print(g[2])
