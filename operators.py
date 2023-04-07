# Python chia các toán tử thành các nhóm sau:
# 1. Toán tử số học (Arithmetic operators)
# 2. Toán tử gán (Assignment operators)
# 3. Toán tử so sánh (Comparison operators)
# 4. Toán tử logic (Logical operators)
# 5. Toán tử nhận dạng (Identity operators)
# 6. Toán tử quan hệ (Membership operators)
# 7. Toán tử bitwise (Bitwise operators)

'''
1. Toán tử số học
 - '+': cộng
 - '-': trừ
 - '*': nhân
 - '/': chia lấy nguyên
 - '%': chia lấy dư
 - '**': lũy thừa
 - '//': chia làm tròn xuống
'''

'''
2. Toán tử gán
 - '=': gán value
 - '+=': ví dụ: x +=1 // x = x + 1
 - '-=': ví dụ: x -=1 // x = x - 1
 - '*=': ví dụ: x *=1 // x = x * 1
 - '/=': ví dụ: x /=1 // x = x / 1
 - '%=': ví dụ: x %=1 // x = x % 1
 - '//=': ví dụ: x //=1 // x = x // 1
 - '**=': ví dụ: x **=1 // x = x ** 1
'''

'''
3. Toán tử so sánh
 - '==': so sánh bằng
 - '!=': so sánh không bằng
 - '>': so sánh lớn hơn
 - '<': so sánh nhỏ hơn
 - '>=': so sánh lớn hơn hoặc bằng
 - '<=': so sánh nhỏ hơn hoặc bằng  
'''

'''
4. Toán tử logic
 - 'and': trả về True nếu cả 2 điều kiện đều đúng.
 - 'or': trả về True nếu 1 trong số đó đúng.
 - 'not': Đảo ngược kết quả, trả về False nếu là True, và ngược lại.
'''

'''
5. Toán tử nhận dạng
# được sử dụng để so sánh các object, không phải nếu chúng bằng nhau, mà nếu chúng thực sự là cùng 1 object, với cùng
một ví trí bộ nhớ.
 - 'is': Trả về True nếu cả 2 biến là cùng 1 object.
 - 'is not': Trả về True nếu cả 2 biến không phải là cùng 1 object.
'''
x = ['orange', 'banana']
y = ['orange', 'banana']
z = x
print(x in z)# True. Vì z cùng object với x
print(x in y)# False. Vì y không cùng object với x, ngay cả khi chúng có cùng nội dung
print(x == y)# True. Vì x bằng y

print(x not in z)#False.
print(x not in y)#True.
print(x != y)#False.

'''
6. Toán tử quan hệ
# được sử dụng để kiểm tra xem một chuỗi có nằm trong 1 object hay không
 - 'in': Return True, nếu 1 chuỗi có giá trị được chỉ định trong 1 object.
 - 'not in': Return True, nếu 1 chuỗi có giá trị đã chỉ định không có trong 1 object. 
'''
x = ["apple", "banana"]
print('banana' in x)# True. vì value banana nằm trong list x
print('orange' not in x)# True. vì value orange không nằm trong list x