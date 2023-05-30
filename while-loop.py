'''
Python có 2 primitive loop
 - while loops
 - for loops
'''

# The while loop
i = 1
while i < 6:
    print(i)# 1 -> 5
    i += 1

# 2. The break statement
i = 1
while i < 6:
    print(i)# 1 -> 3
    if i == 3:
        break
    i +=1

# 3. The continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)# 1 2 4 5 6

# 4. The else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

