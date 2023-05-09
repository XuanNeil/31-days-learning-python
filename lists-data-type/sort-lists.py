'''
Sort Lists
- sort() method sẽ sắp xếp danh sách theo thứ tự chữ và số, tăng dần theo mặc định
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

numberList = [100, 50, 65, 82, 23]
numberList.sort()
print(numberList)#[23, 50, 65, 82, 100]

'''
Sắp xếp giảm dần (descending), sử dụng reverse = True
'''
numberList = [120, 150, 8, 82, 23]
numberList.sort(reverse=True)
print(numberList)#[150, 120, 82, 23, 8]

'''
Customize sort function
'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)# sắp xếp danh sách với mức độ gần của số đó vs 50.
print(thislist)#[50, 65, 23, 82, 100]

'''
Sắp xếp không phân biệt chữ hoa và chữ thường
- theo default, sort() phân biệt chữ hoa chữ thường -> dẫn đến tất cả các chữ in hoa được sắp xếp trước các chữ in thường.
- Vì vậy, nếu muốn sắp xếp không phân biệt chữ hoa chữ thường, hãy sử dụng str.lower
'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)#['Kiwi', 'Orange', 'banana', 'cherry']

thislist.sort(key= str.lower)
print(thislist)#['banana', 'cherry', 'Kiwi', 'Orange']

'''
reverse order
'''
newList = [1, 2, 3, 4, 5]
newList.reverse()
print(newList)#[5, 4, 3, 2, 1]