'''
Tuples
VD: myTuple = ("apple", "banana", "cherry")

- Tuples được sử dụng để lưu trữ nhiều items trong 1 biến.
- Tuples là 1 trong 4 loại dữ liệu được tích hợp trong Python được sử dụng để lưu trữ các bộ sưu tập dữ liệu,
3 loại còn lại là lists, set, dictionary.
- Tuple là 1 bộ sưu tập được sắp xếp theo thứ tự và không hề thay đổi.
- Được biết với dấu ngoặc tròn: ()
'''

# 1. Create a tuple
thisTuple = ("apple", "cherry", "orange")
print(thisTuple)

# 2. Tuple items
# Được sắp xếp theo thứ tự, không thể thay đổi và cho phép các giá trị trùng lặp.

# 3. Ordered
# Khi tuples được sắp xếp theo thứ tự, điều đó có nghĩa là các mục một thứ tự xác định và các thứ tự đó sẽ không thay đổi.

# 4. Unchangeable
# Tuples không thể thay đổi, nghĩa là chúng không thể thêm hoặc xóa các mục sau khi tuple đã được tạo.

# 5. Allow Duplicates
# Vì Tuples được lập index, chúng có thể có các mục có cùng giá trị.
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple1)

# 6. Tuple Length
print(len(tuple1))

# 7. Create tuple with one item
# Để tạo 1 tuple chỉ có 1 index, phải thêm dấu phẩy "," sau mục đó, nếu không Python sẽ không nhận ra nó là 1 Tuple.
oneItemWithTuple = ("apple",)
print(type(oneItemWithTuple))# tuple

test = ("apple")
print(type(test))# str

# 8. Tuple Items - Data types
# Tuple có thể thuộc bất ký kiểu dữ liệu nào, và cũng chứa các kiểu dữ liệu khác nhau.
tuple2 = (1, 5, 7, 8, 9)
tuple3 = ("a", True, 1, "male")

# 9. Type()
myTuple = ("apple", 1, 5, True)
print(type(myTuple))# tuple

# 10. tuple() constructor
tuple4 = tuple(("apple", 1, True, False))
print(tuple4)
