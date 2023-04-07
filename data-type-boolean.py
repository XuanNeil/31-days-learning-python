# Booleans đại diện cho một trong hai giá trị: True or False.
# Hầu hết các giá trị đều được đánh giá là True, nếu nó có nội dung sau:
# 1. Bất kỳ chuỗi nào đều là True, ngoại trừ empty string.
# 2. Bất kỳ số nào đều là True, ngoại từ 0.
# 3. Một list, type, set and dictionary đều là True, ngoại trừ rỗng.

# Giá trị False:
'''
1. False
2. empty value: (), {}, [], ""
3. 0
4. None
'''

# ép về giá trị booleans
print(bool('Hello'))#true
print(bool(15))#true

# Function có thể return a boolean
def myFn():
    return True

print(myFn())

# isinstance() có thể được sử dụng để xác định xem 1 đối tượng có thuộc 1 loại data type hay không
# method return về 1 boolean.
print(isinstance(20, float))
