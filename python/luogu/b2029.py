import math

s = input().split()
r = int(s[1]) / 10
h = int(s[0]) / 10
v = r**2 * 3.14 * h
a = math.ceil(20 / v)
print(a)
"""
a = 20 //v
if 20/v > a:
    print(a+1)
else:
    print(a)
"""
