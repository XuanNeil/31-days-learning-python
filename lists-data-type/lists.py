# List được sử dụng để lưu trữ nhiều items trong một biến duy nhất.
# List là một trong 4 loại dữ liệu built-in được sử dụng để lưu trữ các bộ dữ liệu, 3 loại còn lại là Tuple, Set and Dictionary.
# Danh sách được tạo bằng dấu ngoặc vuông: []

# Có 4 collection data types in Python.
# List: 1 collection được sắp xếp (ordered) và thay đổi (changeable). Cho phép các item trùng lặp.
# Tuple: 1 collection được sắp xếp (ordered) và không thay đổi (unchangeable). Cho phép các item trùng lặp.
# Set: 1 collection không sắp xếp (unordered), không thể thay đổi (nhưng có thể remove hoặc add item) và không được lập index. Không cho phép các item trùng lặp.
# Dictionary: 1 collection được sắp xếp trong thứ tự (ordered) và có thể thay đổi (changeable). Không cho phép các item trùng lặp.

## Kể từ version 3.7, dictionary được sắp xếp (ordered). Trong version 3.6 trở về, dictionary không sắp xếp (unordered).


listFruit = ["apple", 'orange', 'banana']
print(listFruit)

'''
1. len(): độ dài của list
'''
print(len(listFruit))

'''
2. List Items- Data Types
- Các item có thể thuộc bất kỳ data type
'''
list1 = [1, 'banana', True, 30, 'age']

'''
3. type():
'''
myList = [1, 3, 5]
print(type(myList))

'''
4. list() constructor
- Cũng có thể sử dụng constructor list() khi create 1 new list
'''
thisList = list(("apple", "banana", "cherry"))
print(thisList)

'''
5. Access items
'''
print(thisList[0])

'''
6. Negative Indexing 
- Negative indexing sẽ bắt đầu index từ cuối lên.
'''
print(thisList[-1])

'''
7. Range of indexs
- Bạn có thể chỉ định 1 phạm vi index bằng cách chỉ định nơi bắt đầu và nơi kết thúc phạm vị.
- Khi chỉ định một phạm vi, giá trị trả về sẽ là một danh sách mới với các index đã chỉ định.
Lưu ý: không bao gồm index cuối.
'''
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])#['cherry', 'orange', 'kiwi']
print(fruits[:4])#['apple', 'banana', 'cherry', 'orange']
print(fruits[2:])#["cherry", "orange", "kiwi", "melon", "mango"]

'''
8. Range of Negative indexs
- Chỉ định các index phủ định, nếu muốn bắt đầu tìm kiếm từ cuối list
'''
print(fruits[-4: -1])#["orange", "kiwi", "melon"]

'''
9. Check if item exists
'''
if "orange" in fruits:
    print('yes!!!')

'''
10. Change List Items
'''
thislist1 = ["apple", "banana", "cherry"]
thislist1[1] = 'cherry01'
print(thislist1)#["apple", "cherry01", "cherry"]

'''
11. Change a Range of Item Values
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)#["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"]

listFruit2 = ['apple', 'orange', 'kiwi']
listFruit2[1:2] = ['banana', 'cherry']
print(listFruit2)#["apple", "banana", "cherry", "kiwi"]

listFruit3 = ['apple', 'orange', 'cherry']
listFruit3[1:3] = ['watermelon']
print(listFruit3)#["apple", "watermelon"]

'''
12. Insert Items
'''
thislist03 = ["apple", "banana", "cherry"]
thislist03.insert(2, "watermelon")
print(thislist03)#["apple", "banana", "watermelon", "cherry"]

'''
13. Add list items
'''
thislist04 = ["apple", "banana", "cherry"]
thislist04.append('orange')
print(thislist04)#["apple", "banana", "cherry", "orange"]

'''
14. Extend List
'''
thislist05 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist05.extend(tropical)#["apple", "banana", "cherry", "mango", "pineapple", "papaya"]
print(thislist05)


'''
15. Remove specified item
'''
thislistRemove = ["apple", "banana", "cherry"]
thislistRemove.remove('banana')
print(thislistRemove)#["apple", "cherry"]


'''
16. Remove specified index
'''
thislist06 = ["apple", "banana", "cherry"]
thislist06.pop(1)
print(thislist06)#["apple", "banana"]

thislist07 = ["apple", "banana", "cherry"]
del thislist07[0]
print(thislist07)#["banana", "cherry"]

'''
17. Clear list
'''
thislist08 = ["apple", "banana", "cherry"]
thislist08.clear()
print(thislist08)#[]