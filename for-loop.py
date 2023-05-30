'''
For loop
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# 1. Looping through a string
for x in 'banana':
  print(x)

# 2. The break statement
for x in fruits:
  print(x) # apple banana
  if x == "banana":
    break

for x in fruits:
  if x == "banana":
    break
  print(x)# apple

# 3. The continue statement
for x in fruits:
  if x == "banana":
    continue
  print(x)# apple cherry

# 4. The range() function
for x in range(6):
  print(x)# 0 -> 5 not including 6

for x in range(2, 30, 3):
  print(x)# 2 5 8 11 14 17 20 23 26 29

# 5. Else in for loop
# Lưu ý: else sẽ không đc thực thi nếu loop bị stopped bởi break statement
for x in range(6):
  print(x)# 0 -> 5
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)# 0 -> 2
else:
  print("Finally finished!")

# 6. Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
    '''red apple
        red banana
        red cherry
        big apple
        big banana
        big cherry
        tasty apple
        tasty banana
        tasty cherry'''

# 7. The pass statement
for x in [0, 1, 2]:
  pass