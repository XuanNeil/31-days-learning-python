'''
List Comprehension
syntax:
newList = [expression for item in iterable if condition == True]
'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if 'a' in x:
        newList.append(x)

print(newList)#["apple", "banana", "mango"]

# with List Comprehension, có thể làm chỉ với 1 dòng code
newList = [ x for x in fruits if 'a' in x ]
print(newList) #["apple", "banana", "mango"]

#create a lists number 0 -> 9
listNumber = [ x for x in range(10)]
print(listNumber)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

upperList = [x.upper() for x in fruits]
print(upperList)#["APPLE", "BANANA", "CHERRY", "KIWI", "MANGO"]

newList = [ x if x != 'banana' else "orange" for x in fruits ]
print(newList)#['apple', 'orange', 'cherry', 'kiwi', 'mango']