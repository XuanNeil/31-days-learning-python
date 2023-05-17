'''
Add Set Items
'''

thisset = {"apple", "banana", "cherry"}
thisset.add('orange')
print(thisset)#{'apple', 'orange', 'cherry', 'banana'}

'''
Add elements
'''
thisSet = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisSet.update(tropical)
print(thisSet)#{'papaya', 'banana', 'mango', 'cherry', 'pineapple', 'apple'}

'''
Add Any Iterable
'''
fruits = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

fruits.update(mylist)
print(fruits)#{'banana', 'apple', 'orange', 'kiwi', 'cherry'}