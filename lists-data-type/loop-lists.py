'''
Loop List
'''

'''
1. Using for
'''
listFruits = ["apple", "banana", "cherry"]
for fruit in listFruits:
    print(fruit)

'''
2. Lặp qua các index
'''
for i in range(len(listFruits)):
    print(i,listFruits[i])

'''
3. Using a white loop
'''
index = 0
while index < len(listFruits):
    print(index,listFruits[index])
    index += 1

'''
4. Using List Comprehension
'''
[print(fruit) for fruit in listFruits]