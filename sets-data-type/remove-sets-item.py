'''
Remove set items
'''

'''
1. Using remove()
- Lưu ý: Nếu mục cần xóa không tồn tại, remove() sẽ gây ra lỗi
'''
thisset = {"apple", "banana", "cherry"}
thisset.remove('apple')
print(thisset)#{'cherry', 'banana'}

'''
2. Using discard()
- Lưu ý: Nếu mục cần xóa không tồn tại, discard() không gây ra lỗi
'''
fruits = {'apple', 'orange', 'banana'}
fruits.discard('apple')
print(fruits)#{'banana', 'orange'}

'''
3. Using clear()
'''
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)#set()

'''
4. Using del()
'''
