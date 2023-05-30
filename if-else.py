'''
If ... Else
'''
a = 33
b = 200
if b > a:
  print("b is greater than a")


c = 33
d = 33
if c > d:
  print("c is greater than d")
elif c == d:
  print("c and d are equal")

e = 200
f = 33
if f > e:
  print("f is greater than e")
elif e == f:
  print("e and f are equal")
else:
  print("e is greater than f")

# 1. Short hand if
if a < b: print('a > b')
# 2. Short hand if ...else
print("A") if a > b else print("B")

g = 330
h = 330
print("G") if g > h else print("=") if g == h else print("H")