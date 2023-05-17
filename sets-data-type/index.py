'''
Sets
- 1 set là 1 collection không có thứ tự, unchangeable(không thể thay đổi) và không có index.
- Lưu ý: Các item trong set không thể thay đổi(unchangeable) nhưng có thể xóa các item và thêm các item mới.
- Lưu ý: Các giá trị True và 1 được coi là cùng 1 giá trị trong set và được coi là trùng lặp
'''

thisSet = {"apple", "banana", "cherry"}
print(thisSet)#{'apple', 'banana', 'cherry'}

thisSet2 = {"apple", "banana", "cherry", True, 1, 2}
print(thisSet2)#{'apple', True, 'banana', 2, 'cherry'}

'''
Get the length of a Set
'''
print(len(thisSet2))#5

'''
type()
'''
print(type(thisSet2))#<class 'set'>

'''
The set() Constructor
'''
createSet = set(('apple', 'orange', 'cherry'))
print(createSet)#{'cherry', 'orange', 'apple'}

