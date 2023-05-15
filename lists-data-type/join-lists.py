'''
Join Lists
'''
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
thisList = list1 + list2
print(thisList)

# for item in list2:
#     list1.append(item)

# print(list1)

list1.extend(list2)
print(list1)
