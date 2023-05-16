'''
Access Tuple Items
'''

# 1. Access Tuple Items
thisTuple = ("apple", "banana", "cherry")
print(thisTuple[0])#apple

# 2. Negative Indexing
print(thisTuple[-1])#cherry

# 3. Range of Indexs
listTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(listTuple[2:5])#("cherry", "orange", "kiwi")

print(listTuple[:5])#("apple", "banana", "cherry", "orange", "kiwi")

print(listTuple[2:])#("cherry", "orange", "kiwi", "melon", "mango")

# 4. Range of Negative Indexs
print(listTuple[-4:-1])#("orange", "kiwi", "melon")

# 5. Check if Item Exists
if "apple" in listTuple:
    print("Yes!!!")
