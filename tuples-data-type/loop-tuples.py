'''
Loop tuples
'''
# 1. for
thistuple = ("apple", "banana", "cherry")
for item in thistuple:
    print(item)

# 2. Loop through the Index Numbers
for i in range(len(thistuple)):
    print(thistuple[i])

# 3. Using a white loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i +=1
    