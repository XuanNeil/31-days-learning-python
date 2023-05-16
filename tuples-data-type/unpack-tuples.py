'''
Unpack Tuples
'''

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)# apple banana cherry

listFruit = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = listFruit
print(green)#apple
print(yellow)#banana
print(red)#["cherry", "strawberry", "raspberry"]

list = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = list
print(green)#apple
print(tropic)#["mango", "papaya", "pineapple"]
print(red)#cherry

